#!/usr/bin/env python3
"""Build the public, privacy-safe item manifest for a delivered briefing."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
from pathlib import Path
from typing import Any
from urllib.parse import SplitResult, urlsplit, urlunsplit


REPORT_ID_RE = re.compile(r"^\d{4}-\d{2}-\d{2}-(?:morning|evening)$")
ANCHOR_RE = re.compile(r'^<a id="(?P<anchor>item-[^"]+)"></a>$')
ITEM_RE = re.compile(
    r"^### \[(?P<title>.+)\]\((?P<url>https?://.+)\)\s+"
    r"⭐️\s*(?P<score>\d+(?:\.\d+)?)/10\s*$"
)
PROFILE_RE = re.compile(r"^item-(?P<profile>.+)-\d+$")
SOURCE_RE = re.compile(r"^(?P<source>[a-z_]+)\s*·", re.IGNORECASE)
TAGS_RE = re.compile(r"^\*\*(?:태그|Tags|标签)\*\*\s*:\s*(?P<tags>.+)$")


def canonical_url(raw_url: str) -> str | None:
    """Return a stable HTTP(S) URL for identity, or None when it is unsafe."""

    try:
        parts = urlsplit(raw_url.strip())
        if parts.scheme.lower() not in {"http", "https"} or not parts.hostname:
            return None
        host = parts.hostname.lower()
        port = parts.port
        if port and not (
            (parts.scheme.lower() == "http" and port == 80)
            or (parts.scheme.lower() == "https" and port == 443)
        ):
            host = f"{host}:{port}"
        if parts.username or parts.password:
            return None
        normalized = SplitResult(
            scheme=parts.scheme.lower(),
            netloc=host,
            path=parts.path or "/",
            query=parts.query,
            fragment="",
        )
        return urlunsplit(normalized)
    except (TypeError, ValueError):
        return None


def content_key(url: str) -> str:
    return hashlib.sha256(url.encode("utf-8")).hexdigest()


def _clean_text(value: Any, limit: int) -> str:
    if not isinstance(value, str):
        return ""
    return " ".join(value.split())[:limit]


def _clean_score(value: Any) -> float | None:
    try:
        score = float(value)
    except (TypeError, ValueError):
        return None
    if not 0 <= score <= 10:
        return None
    return round(score, 2)


def parse_selected_items(briefing: Path) -> list[dict[str, Any]]:
    """Extract selected entries from the stable anchor/heading pair in Markdown."""

    items: list[dict[str, Any]] = []
    pending_anchor: str | None = None
    current_item: dict[str, Any] | None = None
    for raw_line in briefing.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        anchor_match = ANCHOR_RE.match(line)
        if anchor_match:
            pending_anchor = anchor_match.group("anchor")
            current_item = None
            continue
        if pending_anchor is None:
            if current_item is not None:
                source_match = SOURCE_RE.match(line)
                if source_match and not current_item.get("source_type"):
                    current_item["source_type"] = source_match.group("source").lower()
                tags_match = TAGS_RE.match(line)
                if tags_match:
                    current_item["tags"] = [
                        tag.lstrip("#")
                        for tag in re.findall(r"`([^`]+)`", tags_match.group("tags"))
                    ][:30]
            continue
        item_match = ITEM_RE.match(line)
        if not item_match:
            if line:
                pending_anchor = None
            continue

        url = canonical_url(item_match.group("url"))
        score = _clean_score(item_match.group("score"))
        title = _clean_text(item_match.group("title"), 500)
        if url and score is not None and title:
            profile_match = PROFILE_RE.match(pending_anchor)
            current_item = {
                "id": f"selected:{pending_anchor}",
                "content_key": content_key(url),
                "surface": "selected",
                "anchor_id": pending_anchor,
                "title": title,
                "url": url,
                "score": score,
                "profile": profile_match.group("profile") if profile_match else None,
                "source_type": None,
                "tags": [],
            }
            items.append(current_item)
        pending_anchor = None
    return items


def parse_more_items(
    near_misses: Path | None,
    *,
    minimum_score: float,
    excluded_keys: set[str],
) -> list[dict[str, Any]]:
    if near_misses is None or not near_misses.exists():
        return []
    payload = json.loads(near_misses.read_text(encoding="utf-8"))
    if not isinstance(payload, list):
        raise ValueError("near-misses JSON must contain a list")

    items: list[dict[str, Any]] = []
    seen = set(excluded_keys)
    for raw in payload:
        if not isinstance(raw, dict):
            continue
        url = canonical_url(raw.get("url", ""))
        score = _clean_score(raw.get("score"))
        title = _clean_text(raw.get("title"), 500)
        if not url or score is None or score < minimum_score or not title:
            continue
        key = content_key(url)
        if key in seen:
            continue
        seen.add(key)

        tags = raw.get("tags", [])
        clean_tags = (
            [_clean_text(tag, 80) for tag in tags if _clean_text(tag, 80)][:30]
            if isinstance(tags, list)
            else []
        )
        items.append(
            {
                "id": _clean_text(raw.get("id"), 500) or f"more:{key}",
                "content_key": key,
                "surface": "more",
                "title": title,
                "url": url,
                "score": score,
                "summary": _clean_text(raw.get("summary"), 2000),
                "tags": clean_tags,
                "source_type": _clean_text(raw.get("source_type"), 80) or None,
                "sub_source": _clean_text(raw.get("sub_source"), 200) or None,
                "author": _clean_text(raw.get("author"), 200) or None,
                "published_at": _clean_text(raw.get("published_at"), 80) or None,
                "profile": _clean_text(raw.get("profile"), 80) or None,
            }
        )
    return sorted(
        items,
        key=lambda item: (-item["score"], item["title"].casefold(), item["content_key"]),
    )


def build_manifest(
    briefing: Path,
    near_misses: Path | None,
    report_id: str,
    minimum_score: float,
) -> dict[str, Any]:
    if not REPORT_ID_RE.fullmatch(report_id):
        raise ValueError("report-id must be YYYY-MM-DD-morning or YYYY-MM-DD-evening")
    if not 0 <= minimum_score <= 10:
        raise ValueError("minimum-score must be between 0 and 10")

    selected = parse_selected_items(briefing)
    more = parse_more_items(
        near_misses,
        minimum_score=minimum_score,
        excluded_keys={item["content_key"] for item in selected},
    )
    payload: dict[str, Any] = {
        "schema_version": 1,
        "report_id": report_id,
        "minimum_score": minimum_score,
        "counts": {"selected": len(selected), "more": len(more)},
        "items": [*selected, *more],
    }
    encoded = json.dumps(
        payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    payload["manifest_id"] = hashlib.sha256(encoded).hexdigest()
    return payload


def write_manifest(manifest: dict[str, Any], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = output.with_name(f".{output.name}.tmp")
    temporary.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    os.replace(temporary, output)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--briefing", type=Path, required=True)
    parser.add_argument("--near-misses", type=Path)
    parser.add_argument("--report-id", required=True)
    parser.add_argument("--minimum-score", type=float, default=5.0)
    parser.add_argument("--out", type=Path, required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    manifest = build_manifest(
        args.briefing,
        args.near_misses,
        args.report_id,
        args.minimum_score,
    )
    write_manifest(manifest, args.out)
    print(
        f"Prepared {args.report_id}: "
        f"{manifest['counts']['selected']} selected, {manifest['counts']['more']} more"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Rebuild the reader-interest profile from marks exported out of the review page.

The review page stores one document per marked item in the artifact database.
This turns an export of those documents into data/interests.json, which the
next briefing's scoring prompt carries.

    uv run python scripts/apply-marks.py .sync/marks/
    uv run python scripts/apply-marks.py .sync/marks/ --dry-run

Accepts either a directory of one-document-per-file JSON (what read_db's
out_dir produces) or a single JSON file holding a list of marks.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.processing.interests import (  # noqa: E402
    DEFAULT_PATH,
    Interests,
    load_interests,
    save_interests,
)


def read_marks(source: Path) -> list[dict]:
    if source.is_dir():
        marks = []
        for path in sorted(source.rglob("*.json")):
            with path.open(encoding="utf-8") as f:
                data = json.load(f)
            if isinstance(data, dict):
                marks.append(data)
        return marks

    with source.open(encoding="utf-8") as f:
        data = json.load(f)
    if isinstance(data, list):
        return [row for row in data if isinstance(row, dict)]
    if isinstance(data, dict):
        return [data]
    return []


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="Directory or file of exported marks")
    parser.add_argument("--out", type=Path, default=DEFAULT_PATH)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if not args.source.exists():
        print(f"{args.source} 가 없습니다.")
        return 2

    marks = read_marks(args.source)
    if not marks:
        # An empty export is ambiguous - nothing marked yet, or a failed read.
        # Overwriting a good profile with an empty one would silently undo the
        # reader's history, so refuse and let the operator decide.
        print("마킹이 하나도 없습니다. 기존 프로필을 지우지 않고 그대로 둡니다.")
        return 1

    previous = load_interests(args.out)
    interests = Interests.from_marks(
        marks, datetime.now(timezone.utc).isoformat(timespec="seconds")
    )

    print(f"마킹 {interests.marked_count}건 (이전 {previous.marked_count}건)")
    print("  태그  :", ", ".join(f"{t}({n})" for t, n in interests.tags.items()) or "없음")
    print("  출처  :", ", ".join(f"{s}({n})" for s, n in interests.sources.items()) or "없음")
    print("  최근  :", "; ".join(interests.examples[:3]) or "없음")

    if args.dry_run:
        print("\n--dry-run: 파일을 쓰지 않았습니다.")
        return 0

    path = save_interests(interests, args.out)
    print(f"\n{path} 갱신 완료. 다음 브리핑 채점부터 반영됩니다.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

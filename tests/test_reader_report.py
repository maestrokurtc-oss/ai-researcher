"""Tests for the reader-facing report manifest."""

import json
from pathlib import Path

from scripts.prepare_reader_report import build_manifest, canonical_url


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def contrast_ratio(foreground: str, background: str) -> float:
    def luminance(value: str) -> float:
        channels = [int(value[index : index + 2], 16) / 255 for index in (1, 3, 5)]
        linear = [
            channel / 12.92
            if channel <= 0.04045
            else ((channel + 0.055) / 1.055) ** 2.4
            for channel in channels
        ]
        return 0.2126 * linear[0] + 0.7152 * linear[1] + 0.0722 * linear[2]

    lighter, darker = sorted(
        (luminance(foreground), luminance(background)), reverse=True
    )
    return (lighter + 0.05) / (darker + 0.05)


def test_canonical_url_normalizes_origin_and_removes_fragment():
    assert canonical_url("HTTPS://Example.COM:443/path?q=1#section") == (
        "https://example.com/path?q=1"
    )
    assert canonical_url("javascript:alert(1)") is None
    assert canonical_url("https://user:secret@example.com/private") is None


def test_manifest_contains_selected_and_above_threshold_more_items(tmp_path: Path):
    briefing = tmp_path / "briefing.md"
    briefing.write_text(
        """# Briefing

<a id="item-tech-news-1"></a>
### [선정 콘텐츠](https://example.com/selected#top) ⭐️ 8.0/10

본문
rss · Example Feed · 9월 12일 10:00

**태그**: `#AI`, `#news`
""",
        encoding="utf-8",
    )
    near_misses = tmp_path / "near.json"
    near_misses.write_text(
        json.dumps(
            [
                {
                    "id": "duplicate",
                    "title": "선정 콘텐츠 중복",
                    "url": "https://example.com/selected",
                    "score": 9,
                    "reason": "외부에 노출하면 안 되는 내부 평가 근거",
                },
                {
                    "id": "visible",
                    "title": "기준 이상 콘텐츠",
                    "url": "https://example.com/more",
                    "score": 5,
                    "summary": "독자가 읽을 수 있는 요약",
                    "reason": "외부에 노출하면 안 되는 내부 평가 근거",
                    "tags": ["AI", "research"],
                    "source_type": "rss",
                    "profile": "tech-news",
                },
                {
                    "id": "below",
                    "title": "기준 미달 콘텐츠",
                    "url": "https://example.com/below",
                    "score": 4.9,
                },
            ],
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )

    manifest = build_manifest(
        briefing,
        near_misses,
        "2026-09-12-evening",
        5.0,
    )

    assert manifest["counts"] == {"selected": 1, "more": 1}
    assert len(manifest["manifest_id"]) == 64
    assert manifest["items"][0]["anchor_id"] == "item-tech-news-1"
    assert manifest["items"][0]["profile"] == "tech-news"
    assert manifest["items"][0]["source_type"] == "rss"
    assert manifest["items"][0]["tags"] == ["AI", "news"]
    assert manifest["items"][1]["summary"] == "독자가 읽을 수 있는 요약"
    assert "reason" not in json.dumps(manifest, ensure_ascii=False)


def test_manifest_id_is_stable(tmp_path: Path):
    briefing = tmp_path / "briefing.md"
    briefing.write_text(
        '<a id="item-tech-blog-1"></a>\n'
        "### [Stable](https://example.com/stable) ⭐️ 7.0/10\n",
        encoding="utf-8",
    )

    first = build_manifest(briefing, None, "2026-09-12-morning", 5.0)
    second = build_manifest(briefing, None, "2026-09-12-morning", 5.0)

    assert first == second


def test_feedback_client_times_out_and_links_to_recording_notice():
    javascript = (PROJECT_ROOT / "docs/assets/js/horizon.js").read_text(encoding="utf-8")
    feedback_notice = (PROJECT_ROOT / "docs/feedback.md").read_text(encoding="utf-8")

    assert "new AbortController()" in javascript
    assert "controller.abort()" in javascript
    assert "signal: controller.signal" in javascript
    assert "window.clearTimeout(timeoutId)" in javascript
    assert "setBusy(false)" in javascript
    assert "feedback-info-link" in javascript
    assert "+ '/feedback'" in javascript
    assert "익명으로 기록됩니다" in javascript
    assert "title: 독자 피드백" in feedback_notice


def test_feedback_colors_meet_wcag_aa_contrast():
    stylesheet = (PROJECT_ROOT / "docs/assets/css/horizon.css").read_text(
        encoding="utf-8"
    )

    assert "--hz-text-muted: #686477" in stylesheet
    assert "--hz-text-muted: #9b95ad" in stylesheet
    assert "background: #d4a017; color: #2d2a3e" in stylesheet

    for background in ("#faf8f5", "#f3f0eb", "#f0ede7"):
        assert contrast_ratio("#686477", background) >= 4.5
    for background in ("#1a1726", "#231f33", "#211d30"):
        assert contrast_ratio("#9b95ad", background) >= 4.5
    assert contrast_ratio("#2d2a3e", "#d4a017") >= 4.5

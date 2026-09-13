import json
from pathlib import Path

from src.models import Config


GITHUB_CONFIG_PATH = Path(__file__).resolve().parents[1] / "data" / "config.github.json"


def test_github_config_includes_geeknews_with_full_article_extraction() -> None:
    config = Config.model_validate(
        json.loads(GITHUB_CONFIG_PATH.read_text(encoding="utf-8"))
    )

    geeknews_sources = [
        source for source in config.sources.rss if source.name == "GeekNews"
    ]

    assert len(geeknews_sources) == 1
    source = geeknews_sources[0]
    assert source.enabled is True
    assert str(source.url) == "https://news.hada.io/rss/news"
    assert source.category == "community"
    assert source.profile == "tech-news"
    assert source.content_extractor == "trafilatura"
    assert source.selection_threshold == 6.0
    assert config.sources.rss[0] == source


def test_github_config_expands_the_reader_facing_news_pool() -> None:
    config = Config.model_validate(
        json.loads(GITHUB_CONFIG_PATH.read_text(encoding="utf-8"))
    )

    assert config.processing.profile_settings["tech-news"].threshold == 6.0
    assert config.digest.max_items is not None
    assert config.digest.max_items >= 9

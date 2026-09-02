"""arXiv preprint scraper implementation."""

import asyncio
import logging
import random
import re
from datetime import datetime, timezone
from typing import List, Optional
import calendar

import httpx
import feedparser

from .base import BaseScraper
from ..models import ContentItem, SourceType, ArxivConfig

logger = logging.getLogger(__name__)

API_URL = "https://export.arxiv.org/api/query"

# arXiv answers bursts with 429 and occasionally drops the connection outright.
# Both are transient, and a category lost to one is a whole subject area missing
# from the briefing, so retry before giving up.
MAX_ATTEMPTS = 4
# Upper bound on rows for the single combined request.
MAX_RESULTS_CAP = 400


class _Transient(Exception):
    """A failure worth retrying, as opposed to a malformed query."""

# "http://arxiv.org/abs/2401.12345v2" -> "2401.12345". Dropping the version
# suffix collapses the same paper fetched under several categories into one item.
_ABS_ID = re.compile(r"/abs/(?P<id>[^v\s]+?)(?:v\d+)?$")


class ArxivScraper(BaseScraper):
    """Scraper for arXiv preprints via the public Atom API."""

    def __init__(self, config: ArxivConfig, http_client: httpx.AsyncClient):
        """Initialize arXiv scraper.

        Args:
            config: arXiv source configuration
            http_client: Shared async HTTP client
        """
        super().__init__({"source": config}, http_client)
        self.source = config
        self._keywords = [k.lower() for k in config.boost_keywords]

    async def fetch(self, since: datetime) -> List[ContentItem]:
        """Fetch arXiv preprints submitted since the given time.

        All configured categories are requested as one `OR` query. arXiv asks
        callers to stay under one request every three seconds, and a request
        per category burns that budget fast enough to get the whole source
        rate-limited; one combined query costs a single request no matter how
        many categories are configured.

        Args:
            since: Only fetch papers published after this time

        Returns:
            List[ContentItem]: Fetched content items, newest first and
            deduplicated by arXiv ID
        """
        if not self.source.enabled or not self.source.categories:
            return []

        try:
            body = await self._get_with_retry(self._search_query())
        except Exception as e:
            # A non-retryable failure (a malformed query, say) must not take
            # down the whole run - every other source still has news to report.
            logger.warning("arXiv fetch failed: %s: %s", type(e).__name__, e)
            return []
        if body is None:
            return []

        items: List[ContentItem] = []
        seen: set[str] = set()

        try:
            feed = feedparser.parse(body)
            for entry in feed.entries:
                published_at = self._parse_date(entry)
                if not published_at:
                    continue
                # Results are newest-first, so the first old paper ends the page.
                if published_at < since:
                    break

                item = self._build_item(entry, published_at)
                # A cross-listed paper can appear once per matching category.
                if item and item.id not in seen:
                    seen.add(item.id)
                    items.append(item)
        except Exception as e:
            logger.warning(
                "Error parsing arXiv feed: %s: %s", type(e).__name__, e
            )

        return items

    def _search_query(self) -> str:
        """Build the combined `cat:` disjunction for all configured categories."""
        return " OR ".join(f"cat:{c}" for c in self.source.categories)

    def _max_results(self) -> int:
        """Total rows to request for the combined query."""
        # Categories overlap heavily, so the union needs far less than the
        # naive per-category sum; the cap keeps one request from going huge.
        return min(
            self.source.max_results_per_category * len(self.source.categories),
            MAX_RESULTS_CAP,
        )

    async def _get_with_retry(self, search_query: str) -> Optional[str]:
        """Fetch the result page, retrying transient failures.

        Args:
            search_query: arXiv `search_query` expression

        Returns:
            Optional[str]: The Atom body, or None once the retries are spent.
        """
        params = {
            "search_query": search_query,
            "sortBy": "submittedDate",
            "sortOrder": "descending",
            "start": 0,
            "max_results": self._max_results(),
        }

        for attempt in range(1, MAX_ATTEMPTS + 1):
            try:
                response = await self.client.get(
                    API_URL, params=params, follow_redirects=True
                )
                # Only rate limiting and server faults are worth another try.
                # A 4xx other than 429 means the query itself is wrong, so let
                # raise_for_status surface it to the caller immediately.
                if response.status_code == 429 or response.status_code >= 500:
                    raise _Transient(f"HTTP {response.status_code}")
                response.raise_for_status()
                return response.text
            except (_Transient, httpx.TransportError) as e:
                if attempt == MAX_ATTEMPTS:
                    logger.warning(
                        "arXiv fetch failed after %d attempts: %s: %s",
                        MAX_ATTEMPTS, type(e).__name__, e,
                    )
                    return None
                # Exponential backoff from the configured delay, jittered so
                # concurrent categories do not retry in lockstep.
                base = max(self.source.request_delay_sec, 1.0)
                delay = base * (2 ** (attempt - 1)) + random.uniform(0, 1)
                logger.info(
                    "arXiv attempt %d/%d failed (%s); retrying in %.1fs",
                    attempt, MAX_ATTEMPTS, type(e).__name__, delay,
                )
                await asyncio.sleep(delay)

        return None

    def _build_item(
        self, entry: dict, published_at: datetime
    ) -> Optional[ContentItem]:
        """Convert one Atom entry into a ContentItem.

        Args:
            entry: Feed entry data
            published_at: Parsed submission time

        Returns:
            Optional[ContentItem]: None when the entry carries no usable arXiv ID
        """
        raw_id = entry.get("id", "")
        match = _ABS_ID.search(str(raw_id))
        if not match:
            return None
        arxiv_id = match.group("id")

        title = _collapse(entry.get("title", "Untitled"))
        abstract = _collapse(entry.get("summary", ""))
        authors = [a.get("name", "") for a in entry.get("authors", []) if a.get("name")]

        tags = [t.term for t in entry.get("tags", []) if getattr(t, "term", None)]
        primary = entry.get("arxiv_primary_category", {}).get("term") or (
            tags[0] if tags else "unknown"
        )

        haystack = f"{title}\n{abstract}".lower()
        matched = [k for k in self._keywords if k in haystack]

        return ContentItem(
            id=self._generate_id("arxiv", "paper", arxiv_id),
            source_type=SourceType.ARXIV,
            title=title,
            url=f"https://arxiv.org/abs/{arxiv_id}",
            content=abstract,
            author=", ".join(authors[:5]) or None,
            published_at=published_at,
            profile=self.source.profile,
            metadata={
                "feed_name": f"arXiv {primary}",
                "category": self.source.category,
                "arxiv_id": arxiv_id,
                "primary_category": primary,
                "authors": authors,
                "author_count": len(authors),
                "pdf_url": f"https://arxiv.org/pdf/{arxiv_id}",
                # Surfaced for AI scoring; deliberately not a hard filter.
                "matched_keywords": matched,
                "tags": tags,
            },
        )

    def _parse_date(self, entry: dict) -> Optional[datetime]:
        """Parse the submission date from an Atom entry.

        Args:
            entry: Feed entry data

        Returns:
            Optional[datetime]: Parsed submission time in UTC, or None
        """
        for field in ["published", "updated"]:
            parsed = entry.get(f"{field}_parsed")
            if parsed:
                try:
                    return datetime.fromtimestamp(calendar.timegm(parsed), tz=timezone.utc)
                except Exception:
                    continue
        return None


def _collapse(text: str) -> str:
    """Flatten the hard-wrapped whitespace arXiv uses in titles and abstracts."""
    return re.sub(r"\s+", " ", text or "").strip()

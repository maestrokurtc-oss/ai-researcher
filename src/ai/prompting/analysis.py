"""Prompt construction for profile-driven content analysis."""

from ...models import ContentItem
from ...processing.profiles import LoadedProfile
from .common import EVIDENCE_RULES, UNTRUSTED_INPUT_RULE
from .enrichment import target_language_instruction

ANALYSIS_RULES = f"""You are a content curator evaluating an item under the supplied processing profile.

- {UNTRUSTED_INPUT_RULE}
- Base the analysis only on the supplied item and its metadata.
{EVIDENCE_RULES}
- Apply the profile's evaluation policy consistently."""


def analysis_system_prompt(profile: LoadedProfile, language: str = "en") -> str:
    # `summary` is shown to the reader whenever enrichment is skipped or fails,
    # so it has to be written in the briefing's language. `reason` is internal
    # and `tags` are slugs, so both stay English.
    summary_language = (
        f"<one-sentence summary, written in {target_language_instruction(language)}>"
    )
    return f"""{ANALYSIS_RULES}

# Profile policy

{profile.analysis_prompt}

# Output contract

Return valid JSON only. Write `summary` in {target_language_instruction(language)};
keep `reason` in English and `tags` as lowercase hyphenated English slugs.
{{
  "score": <number from 0 to 10>,
  "reason": "<concise explanation, in English>",
  "summary": "{summary_language}",
  "tags": ["<tag>", "..."]
}}"""


def analysis_user_prompt(
    item: ContentItem,
    content_section: str,
    discussion_section: str,
) -> str:
    return f"""Analyze the following content.

Title: {item.title}
Source: {item.source_type.value}
Author: {item.author or "Unknown"}
URL: {item.url}
{content_section}
{discussion_section}"""

"""Estimate Anthropic credit runway and deliver low-balance alerts."""

from __future__ import annotations

import json
import smtplib
import ssl
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from decimal import Decimal
from email.message import EmailMessage
from pathlib import Path

from .._file_utils import _atomic_write_text


@dataclass(frozen=True)
class CreditStatus:
    baseline_usd: Decimal
    spent_usd: Decimal
    remaining_usd: Decimal
    expected_run_usd: Decimal
    warning_threshold_usd: Decimal
    estimated_runs_remaining: Decimal
    record_count: int
    should_alert: bool


def parse_utc_datetime(value: str) -> datetime:
    parsed = datetime.fromisoformat(value.strip().replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def load_costs(usage_root: Path, since: datetime) -> list[Decimal]:
    """Load successful-run estimates created on or after the balance baseline."""
    records: list[tuple[datetime, Decimal]] = []
    if not usage_root.exists():
        return []

    for path in sorted(usage_root.rglob("*.json")):
        if path.name.startswith("."):
            continue
        try:
            record = json.loads(path.read_text(encoding="utf-8"))
            generated_at = parse_utc_datetime(record["generated_at"])
            cost = Decimal(str(record["estimated_cost_usd"]))
        except (OSError, KeyError, ValueError, TypeError, json.JSONDecodeError):
            # A malformed historical record must not take the briefing down.
            # It remains visible in git for manual repair.
            continue
        if generated_at >= since and cost >= 0:
            records.append((generated_at, cost))
    records.sort(key=lambda record: record[0])
    return [cost for _, cost in records]


def calculate_credit_status(
    *,
    baseline_usd: Decimal,
    costs: list[Decimal],
    minimum_warning_usd: Decimal = Decimal("2"),
    reserve_runs: int = 4,
    minimum_expected_run_usd: Decimal = Decimal("0.50"),
) -> CreditStatus:
    if baseline_usd < 0:
        raise ValueError("credit baseline must not be negative")
    if minimum_warning_usd < 0 or minimum_expected_run_usd <= 0:
        raise ValueError("credit guard thresholds must be positive")
    if reserve_runs < 1:
        raise ValueError("credit reserve runs must be at least one")

    spent = sum(costs, Decimal("0"))
    recent = costs[-4:]
    recent_average = (
        sum(recent, Decimal("0")) / Decimal(len(recent))
        if recent
        else Decimal("0")
    )
    # A floor keeps the first few runs conservative and prevents one unusually
    # cheap briefing from promising more runway than is prudent.
    expected_run = max(minimum_expected_run_usd, recent_average)
    remaining = baseline_usd - spent
    warning_threshold = max(
        minimum_warning_usd, expected_run * Decimal(reserve_runs)
    )
    runs_remaining = max(Decimal("0"), remaining) / expected_run

    return CreditStatus(
        baseline_usd=baseline_usd,
        spent_usd=spent,
        remaining_usd=remaining,
        expected_run_usd=expected_run,
        warning_threshold_usd=warning_threshold,
        estimated_runs_remaining=runs_remaining,
        record_count=len(costs),
        should_alert=remaining <= warning_threshold,
    )


def alert_is_due(
    state_path: Path,
    *,
    baseline_at: datetime,
    now: datetime,
    cooldown_hours: int,
) -> bool:
    if cooldown_hours < 0:
        raise ValueError("alert cooldown must not be negative")
    try:
        state = json.loads(state_path.read_text(encoding="utf-8"))
        if state.get("baseline_at") != baseline_at.isoformat():
            return True
        last_alert = parse_utc_datetime(state["last_alert_at"])
    except (OSError, KeyError, ValueError, TypeError, json.JSONDecodeError):
        return True
    return now - last_alert >= timedelta(hours=cooldown_hours)


def save_alert_state(
    state_path: Path,
    *,
    baseline_at: datetime,
    now: datetime,
) -> None:
    state_path.parent.mkdir(parents=True, exist_ok=True)
    state = {
        "baseline_at": baseline_at.isoformat(),
        "last_alert_at": now.astimezone(timezone.utc).isoformat(),
    }
    _atomic_write_text(
        state_path, json.dumps(state, ensure_ascii=False, indent=2) + "\n"
    )


def send_email_alert(
    *,
    username: str,
    app_password: str,
    recipient: str,
    subject: str,
    body: str,
    smtp_server: str = "smtp.gmail.com",
    smtp_port: int = 465,
) -> None:
    """Send a plain-text alert through Gmail's TLS SMTP endpoint."""
    if not username or not app_password or not recipient:
        raise ValueError(
            "Gmail alert credentials are incomplete; set GMAIL_APP_PASSWORD"
        )

    message = EmailMessage()
    message["Subject"] = subject
    message["From"] = f"AI Researcher Alert <{username}>"
    message["To"] = recipient
    message.set_content(body)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(
        smtp_server, smtp_port, context=context, timeout=20
    ) as server:
        server.login(username, app_password.replace(" ", ""))
        server.send_message(message)

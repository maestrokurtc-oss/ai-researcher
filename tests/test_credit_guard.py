"""Credit runway estimation and Gmail alert behavior."""

from __future__ import annotations

import json
from datetime import datetime, timedelta, timezone
from decimal import Decimal

from src.services.credit_guard import (
    alert_is_due,
    calculate_credit_status,
    load_costs,
    save_alert_state,
    send_email_alert,
)


def _record(path, generated_at: str, cost: str) -> None:  # type: ignore[no-untyped-def]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(
            {"generated_at": generated_at, "estimated_cost_usd": cost}
        ),
        encoding="utf-8",
    )


def test_load_costs_ignores_records_before_baseline_and_state(tmp_path) -> None:
    usage = tmp_path / "usage"
    _record(usage / "2026-09-11.json", "2026-09-11T00:00:00Z", "0.30")
    _record(usage / "2026-09-12.json", "2026-09-12T12:00:00Z", "0.40")
    _record(usage / ".credit-alert-state.json", "2026-09-12T12:00:00Z", "99")

    costs = load_costs(
        usage, datetime(2026, 9, 12, tzinfo=timezone.utc)
    )

    assert costs == [Decimal("0.40")]


def test_load_costs_uses_generation_order_not_filename_order(tmp_path) -> None:
    usage = tmp_path / "usage"
    _record(usage / "z.json", "2026-09-12T01:00:00Z", "0.10")
    _record(usage / "a.json", "2026-09-12T02:00:00Z", "0.20")

    costs = load_costs(usage, datetime(2026, 9, 12, tzinfo=timezone.utc))

    assert costs == [Decimal("0.10"), Decimal("0.20")]


def test_status_warns_with_four_conservative_runs_left() -> None:
    status = calculate_credit_status(
        baseline_usd=Decimal("5"),
        costs=[Decimal("1"), Decimal("1"), Decimal("1")],
        minimum_warning_usd=Decimal("2"),
        reserve_runs=4,
        minimum_expected_run_usd=Decimal("0.50"),
    )

    assert status.remaining_usd == Decimal("2")
    assert status.expected_run_usd == Decimal("1")
    assert status.warning_threshold_usd == Decimal("4")
    assert status.estimated_runs_remaining == Decimal("2")
    assert status.should_alert is True


def test_status_does_not_warn_with_healthy_reserve() -> None:
    status = calculate_credit_status(
        baseline_usd=Decimal("10"), costs=[Decimal("0.25")]
    )

    assert status.expected_run_usd == Decimal("0.50")
    assert status.should_alert is False


def test_alert_state_enforces_cooldown_and_resets_with_new_baseline(tmp_path) -> None:
    state = tmp_path / "usage" / ".credit-alert-state.json"
    baseline = datetime(2026, 9, 12, tzinfo=timezone.utc)
    now = baseline + timedelta(hours=2)
    save_alert_state(
        state,
        baseline_at=baseline,
        now=now,
    )

    assert not alert_is_due(
        state,
        baseline_at=baseline,
        now=now + timedelta(hours=23),
        cooldown_hours=24,
    )
    assert alert_is_due(
        state,
        baseline_at=baseline,
        now=now + timedelta(hours=24),
        cooldown_hours=24,
    )
    assert alert_is_due(
        state,
        baseline_at=baseline + timedelta(days=1),
        now=now + timedelta(hours=3),
        cooldown_hours=24,
    )


def test_send_email_alert_uses_gmail_app_password(monkeypatch) -> None:
    calls: dict[str, object] = {}

    class FakeSMTP:
        def __init__(self, server, port, **kwargs):  # type: ignore[no-untyped-def]
            calls["connection"] = (server, port, kwargs)

        def __enter__(self):
            return self

        def __exit__(self, *_):
            return False

        def login(self, username, password):  # type: ignore[no-untyped-def]
            calls["login"] = (username, password)

        def send_message(self, message):  # type: ignore[no-untyped-def]
            calls["message"] = message

    monkeypatch.setattr(
        "src.services.credit_guard.smtplib.SMTP_SSL", FakeSMTP
    )

    send_email_alert(
        username="maestrokurtc@gmail.com",
        app_password="abcd efgh ijkl mnop",
        recipient="maestrokurtc@gmail.com",
        subject="Low credit",
        body="Top up soon",
    )

    assert calls["login"] == ("maestrokurtc@gmail.com", "abcdefghijklmnop")
    message = calls["message"]
    assert message["To"] == "maestrokurtc@gmail.com"
    assert "Top up soon" in message.get_content()

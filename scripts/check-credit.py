#!/usr/bin/env python3
"""Check estimated Anthropic credit runway and send a Gmail alert.

Anthropic exposes billing history but not prepaid balance through a regular API
key. This guard therefore starts from a user-supplied Console balance and
subtracts the per-run model/token estimates archived by the briefing workflow.
"""

from __future__ import annotations

import argparse
import os
import sys
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.services.credit_guard import (
    alert_is_due,
    calculate_credit_status,
    load_costs,
    parse_utc_datetime,
    save_alert_state,
    send_email_alert,
)


DEFAULT_RECIPIENT = "maestrokurtc@gmail.com"


def _decimal_env(name: str, default: str | None = None) -> Decimal:
    raw = os.getenv(name, default)
    if raw is None or not raw.strip():
        raise ValueError(f"{name} is not set")
    try:
        return Decimal(raw.strip())
    except InvalidOperation as exc:
        raise ValueError(f"{name} must be a USD number") from exc


def _int_env(name: str, default: int) -> int:
    raw = os.getenv(name, str(default))
    try:
        return int(raw)
    except ValueError as exc:
        raise ValueError(f"{name} must be an integer") from exc


def _send(subject: str, body: str) -> None:
    recipient = os.getenv("CREDIT_ALERT_EMAIL_TO", DEFAULT_RECIPIENT).strip()
    username = os.getenv("GMAIL_SMTP_USERNAME", DEFAULT_RECIPIENT).strip()
    password = os.getenv("GMAIL_APP_PASSWORD", "")
    send_email_alert(
        username=username,
        app_password=password,
        recipient=recipient,
        subject=subject,
        body=body,
    )
    print(f"Credit alert email sent to {recipient}.")


def _run_url() -> str:
    server = os.getenv("GITHUB_SERVER_URL", "https://github.com")
    repository = os.getenv("GITHUB_REPOSITORY", "maestrokurtc-oss/ai-researcher")
    run_id = os.getenv("GITHUB_RUN_ID", "")
    return f"{server}/{repository}/actions/runs/{run_id}" if run_id else server


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--force-alert",
        action="store_true",
        help="send a test warning regardless of the calculated balance",
    )
    parser.add_argument(
        "--pipeline-failure",
        action="store_true",
        help="send an immediate workflow failure alert",
    )
    args = parser.parse_args()

    if args.pipeline_failure:
        _send(
            "[AI Researcher] 브리핑/API 실행 실패",
            "AI Researcher 실행이 실패했습니다. Anthropic 크레딧, API 키, "
            f"워크스페이스와 실행 로그를 확인하세요.\n\n{_run_url()}\n",
        )
        return 0

    if args.force_alert:
        _send(
            "[AI Researcher] 크레딧 경고 메일 테스트",
            "Gmail 크레딧 경고 채널이 정상적으로 연결되었습니다.\n\n"
            f"실행: {_run_url()}\n",
        )
        return 0

    baseline_raw = os.getenv("ANTHROPIC_CREDIT_BASELINE_USD", "").strip()
    baseline_at_raw = os.getenv("ANTHROPIC_CREDIT_BASELINE_AT", "").strip()
    if not baseline_raw or not baseline_at_raw:
        print(
            "Credit runway check is not configured; set "
            "ANTHROPIC_CREDIT_BASELINE_USD and ANTHROPIC_CREDIT_BASELINE_AT."
        )
        return 0

    baseline = _decimal_env("ANTHROPIC_CREDIT_BASELINE_USD")
    baseline_at = parse_utc_datetime(baseline_at_raw)
    costs = load_costs(Path("usage"), baseline_at)
    status = calculate_credit_status(
        baseline_usd=baseline,
        costs=costs,
        minimum_warning_usd=_decimal_env(
            "ANTHROPIC_CREDIT_WARN_BELOW_USD", "2.00"
        ),
        reserve_runs=_int_env("ANTHROPIC_CREDIT_RESERVE_RUNS", 4),
        minimum_expected_run_usd=_decimal_env(
            "ANTHROPIC_EXPECTED_RUN_COST_USD", "0.50"
        ),
    )

    print(
        "Anthropic credit estimate: "
        f"runway={status.estimated_runs_remaining:.1f} runs, "
        f"records={status.record_count}, "
        f"alert={'yes' if status.should_alert else 'no'}."
    )
    if not status.should_alert:
        return 0

    now = datetime.now(timezone.utc)
    state_path = Path("usage/.credit-alert-state.json")
    cooldown = _int_env("ANTHROPIC_CREDIT_ALERT_COOLDOWN_HOURS", 24)
    if not alert_is_due(
        state_path,
        baseline_at=baseline_at,
        now=now,
        cooldown_hours=cooldown,
    ):
        print("Credit is low, but an alert was already sent within the cooldown.")
        return 0

    _send(
        "[AI Researcher] Anthropic 크레딧 부족 예상",
        "다음 브리핑들이 실패하기 전에 Anthropic API 크레딧을 확인해 주세요.\n\n"
        f"기준 잔액: ${status.baseline_usd:.2f}\n"
        f"추적 사용액: ${status.spent_usd:.4f}\n"
        f"예상 잔액: ${status.remaining_usd:.4f}\n"
        f"예상 잔여 회차: {status.estimated_runs_remaining:.1f}회\n"
        f"경고 기준: ${status.warning_threshold_usd:.4f}\n\n"
        "Anthropic Console의 Billing 페이지에서 실제 잔액을 확인하고, 충전 후 "
        "기준 잔액과 기준 시각을 갱신하세요.\n\n"
        f"실행: {_run_url()}\n",
    )
    save_alert_state(
        state_path,
        baseline_at=baseline_at,
        now=now,
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"Credit guard failed: {type(exc).__name__}: {exc}", file=sys.stderr)
        raise SystemExit(2)

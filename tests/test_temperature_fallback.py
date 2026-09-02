"""Newer Claude models reject `temperature`; the client must adapt, not fail."""

from __future__ import annotations

import asyncio
from types import SimpleNamespace

import pytest

from src.ai.client import AnthropicClient, _is_temperature_deprecated
from src.models import AIConfig, AIProvider

DEPRECATED = "Error code: 400 - {'message': '`temperature` is deprecated for this model.'}"


def _config(**overrides):  # type: ignore[no-untyped-def]
    values = {
        "provider": AIProvider.ANTHROPIC,
        "model": "claude-sonnet-5",
        "api_key_env": "ANTHROPIC_API_KEY",
        "temperature": 0.3,
    }
    values.update(overrides)
    return AIConfig(**values)


def _client(monkeypatch, create):  # type: ignore[no-untyped-def]
    monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-test")
    monkeypatch.delenv("ANTHROPIC_WORKSPACE_ID", raising=False)
    monkeypatch.setattr(
        "src.ai.client.AsyncAnthropic",
        lambda **_: SimpleNamespace(messages=SimpleNamespace(create=create)),
    )
    return AnthropicClient(_config())


def _message(text: str = "ok"):  # type: ignore[no-untyped-def]
    return SimpleNamespace(
        content=[SimpleNamespace(type="text", text=text)],
        usage=SimpleNamespace(input_tokens=10, output_tokens=2),
    )


def test_detects_the_deprecation_message() -> None:
    assert _is_temperature_deprecated(DEPRECATED)
    assert _is_temperature_deprecated("temperature is not supported")
    assert not _is_temperature_deprecated("overloaded_error")
    # Must not swallow an unrelated 400.
    assert not _is_temperature_deprecated("max_tokens is deprecated")


def test_retries_without_temperature_and_remembers(monkeypatch) -> None:  # type: ignore[no-untyped-def]
    calls: list[dict] = []

    async def create(**kwargs):  # type: ignore[no-untyped-def]
        calls.append(kwargs)
        if "temperature" in kwargs:
            raise RuntimeError(DEPRECATED)
        return _message()

    client = _client(monkeypatch, create)

    assert asyncio.run(client.complete(system="s", user="u")) == "ok"
    assert len(calls) == 2
    assert "temperature" in calls[0] and "temperature" not in calls[1]

    # The second call must not repeat the doomed attempt.
    assert asyncio.run(client.complete(system="s", user="u")) == "ok"
    assert len(calls) == 3
    assert "temperature" not in calls[2]


def test_unrelated_errors_still_propagate(monkeypatch) -> None:  # type: ignore[no-untyped-def]
    async def create(**_):  # type: ignore[no-untyped-def]
        raise RuntimeError("Error code: 529 - overloaded_error")

    client = _client(monkeypatch, create)

    with pytest.raises(RuntimeError, match="overloaded"):
        asyncio.run(client.complete(system="s", user="u"))


def test_models_that_accept_temperature_keep_sending_it(monkeypatch) -> None:  # type: ignore[no-untyped-def]
    calls: list[dict] = []

    async def create(**kwargs):  # type: ignore[no-untyped-def]
        calls.append(kwargs)
        return _message()

    client = _client(monkeypatch, create)
    asyncio.run(client.complete(system="s", user="u"))
    asyncio.run(client.complete(system="s", user="u"))

    assert all("temperature" in c for c in calls)

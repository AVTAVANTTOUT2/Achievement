"""Tests du formatage de rapport."""

from __future__ import annotations

from pathlib import Path

from repoaudit.checks import CheckResult
from repoaudit.report import format_report


def test_format_report_includes_score_and_status() -> None:
    results = [
        CheckResult("README", True, "ok"),
        CheckResult("Licence", False, "manquant"),
    ]
    text = format_report(Path("/tmp/demo"), results)
    assert "Score : 1/2" in text
    assert "50%" in text
    assert "[✓] README" in text
    assert "[✗] Licence" in text
    assert "insuffisant" in text or "correct" in text


def test_format_report_excellent_when_perfect() -> None:
    results = [
        CheckResult("README", True, "ok"),
        CheckResult("Licence", True, "ok"),
    ]
    text = format_report(Path("."), results)
    assert "100%" in text
    assert "excellent" in text

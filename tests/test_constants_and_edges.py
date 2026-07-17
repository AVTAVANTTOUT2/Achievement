"""Tests des constantes et cas limites supplémentaires."""

from __future__ import annotations

from pathlib import Path

from repoaudit.checks import check_license, check_readme, check_workflows
from repoaudit.constants import EXIT_INVALID_PATH, EXIT_STRICT_FAILURE, EXIT_SUCCESS, MIN_README_BYTES


def test_exit_codes_are_distinct() -> None:
    assert len({EXIT_SUCCESS, EXIT_STRICT_FAILURE, EXIT_INVALID_PATH}) == 3


def test_readme_accepts_exact_minimum_size(tmp_path: Path) -> None:
    content = "x" * MIN_README_BYTES
    (tmp_path / "README.md").write_text(content, encoding="utf-8")
    assert check_readme(tmp_path).passed is True


def test_license_txt_is_detected(tmp_path: Path) -> None:
    (tmp_path / "LICENSE.txt").write_text("MIT License\n", encoding="utf-8")
    assert check_license(tmp_path).passed is True


def test_workflows_empty_directory_fails(tmp_path: Path) -> None:
    (tmp_path / ".github" / "workflows").mkdir(parents=True)
    result = check_workflows(tmp_path)
    assert result.passed is False
    assert "Aucun workflow" in result.detail

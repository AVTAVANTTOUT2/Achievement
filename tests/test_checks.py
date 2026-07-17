"""Tests des vérifications de qualité."""

from __future__ import annotations

from pathlib import Path

from repoaudit.checks import (
    check_community_files,
    check_license,
    check_readme,
    check_tests,
    check_workflows,
    run_all_checks,
    score,
)


def test_check_readme_passes_when_present(tmp_path: Path) -> None:
    (tmp_path / "README.md").write_text(
        "# Projet\n\nDescription utile du dépôt pour l'audit communautaire.\n",
        encoding="utf-8",
    )
    result = check_readme(tmp_path)
    assert result.passed is True
    assert "README.md" in result.detail


def test_check_readme_fails_when_missing(tmp_path: Path) -> None:
    result = check_readme(tmp_path)
    assert result.passed is False


def test_check_license_passes(tmp_path: Path) -> None:
    (tmp_path / "LICENSE").write_text("MIT License\n", encoding="utf-8")
    assert check_license(tmp_path).passed is True


def test_check_community_files_partial(tmp_path: Path) -> None:
    (tmp_path / "CONTRIBUTING.md").write_text("# Contribuer\n", encoding="utf-8")
    result = check_community_files(tmp_path)
    assert result.passed is False
    assert "CONTRIBUTING" in result.detail
    assert "SECURITY" in result.detail


def test_check_tests_detects_pytest_files(tmp_path: Path) -> None:
    tests = tmp_path / "tests"
    tests.mkdir()
    (tests / "test_sample.py").write_text("def test_ok():\n    assert True\n", encoding="utf-8")
    result = check_tests(tmp_path)
    assert result.passed is True


def test_check_workflows_detects_yaml(tmp_path: Path) -> None:
    workflows = tmp_path / ".github" / "workflows"
    workflows.mkdir(parents=True)
    (workflows / "ci.yml").write_text("name: ci\non: push\n", encoding="utf-8")
    result = check_workflows(tmp_path)
    assert result.passed is True
    assert "ci.yml" in result.detail


def test_run_all_checks_and_score(tmp_path: Path) -> None:
    (tmp_path / "README.md").write_text(
        "# Demo\n\nContenu suffisant pour passer le seuil minimal README du projet.\n",
        encoding="utf-8",
    )
    (tmp_path / "LICENSE").write_text("MIT\n", encoding="utf-8")
    results = run_all_checks(tmp_path)
    assert len(results) == 5
    obtained, maximum = score(results)
    assert maximum >= obtained
    assert obtained >= 2

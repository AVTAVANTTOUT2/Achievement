"""Tests du point d'entrée CLI."""

from __future__ import annotations

from pathlib import Path

from repoaudit.cli import main


def test_main_prints_report(tmp_path: Path, capsys) -> None:
    (tmp_path / "README.md").write_text(
        "# Demo\n\nDescription assez longue pour valider le CLI.\n",
        encoding="utf-8",
    )
    code = main([str(tmp_path)])
    captured = capsys.readouterr()
    assert code == 0
    assert "repoaudit" in captured.out
    assert "Score" in captured.out


def test_main_strict_fails_incomplete_repo(tmp_path: Path) -> None:
    (tmp_path / "README.md").write_text(
        "# Demo\n\nDescription assez longue pour valider le CLI.\n",
        encoding="utf-8",
    )
    code = main(["--strict", str(tmp_path)])
    assert code == 1


def test_main_missing_path_returns_2(tmp_path: Path) -> None:
    code = main([str(tmp_path / "does-not-exist")])
    assert code == 2

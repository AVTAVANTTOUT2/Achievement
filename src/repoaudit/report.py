"""Formatage du rapport terminal."""

from __future__ import annotations

from pathlib import Path

from repoaudit.checks import CheckResult, score


def format_report(root: Path, results: list[CheckResult]) -> str:
    """Construit un rapport lisible pour le terminal."""
    obtained, maximum = score(results)
    percent = 0 if maximum == 0 else round(100 * obtained / maximum)
    lines = [
        "repoaudit — rapport de qualité du dépôt",
        f"Cible : {root.resolve()}",
        "─" * 48,
    ]
    for result in results:
        mark = "✓" if result.passed else "✗"
        lines.append(f"[{mark}] {result.name}: {result.detail}")
    lines.extend(
        [
            "─" * 48,
            f"Score : {obtained}/{maximum} ({percent}%)",
        ]
    )
    if percent == 100:
        lines.append("Statut : excellent — critères communautaires couverts.")
    elif percent >= 60:
        lines.append("Statut : correct — quelques améliorations restantes.")
    else:
        lines.append("Statut : insuffisant — priorisez README, licence et tests.")
    return "\n".join(lines)

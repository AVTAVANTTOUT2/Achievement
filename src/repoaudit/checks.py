"""Vérifications de qualité pour un dépôt GitHub local."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from repoaudit.constants import (
    CODE_OF_CONDUCT_NAMES,
    CONTRIBUTING_NAMES,
    LICENSE_NAMES,
    MIN_README_BYTES,
    README_NAMES,
    SECURITY_NAMES,
    TEST_MARKERS,
    WORKFLOW_DIR,
)


@dataclass(frozen=True)
class CheckResult:
    """Résultat d'une vérification individuelle."""

    name: str
    passed: bool
    detail: str
    weight: int = 1


def _exists_any(root: Path, names: tuple[str, ...]) -> Path | None:
    for name in names:
        candidate = root / name
        if candidate.is_file():
            return candidate
    return None


def check_readme(root: Path) -> CheckResult:
    found = _exists_any(root, README_NAMES)
    if found is None:
        return CheckResult("README", False, "Aucun fichier README trouvé")
    size = found.stat().st_size
    if size < MIN_README_BYTES:
        return CheckResult("README", False, f"{found.name} trop court ({size} octets)")
    return CheckResult("README", True, f"Présent: {found.name} ({size} octets)")


def check_license(root: Path) -> CheckResult:
    found = _exists_any(root, LICENSE_NAMES)
    if found is None:
        return CheckResult("Licence", False, "Aucun fichier LICENSE trouvé")
    return CheckResult("Licence", True, f"Présent: {found.name}")


def check_community_files(root: Path) -> CheckResult:
    present: list[str] = []
    missing: list[str] = []
    for label, names in (
        ("CONTRIBUTING", CONTRIBUTING_NAMES),
        ("CODE_OF_CONDUCT", CODE_OF_CONDUCT_NAMES),
        ("SECURITY", SECURITY_NAMES),
    ):
        if _exists_any(root, names):
            present.append(label)
        else:
            missing.append(label)
    if not present:
        return CheckResult(
            "Fichiers communautaires",
            False,
            f"Manquants: {', '.join(missing)}",
            weight=2,
        )
    detail = f"Présents: {', '.join(present)}"
    if missing:
        detail += f" | Manquants: {', '.join(missing)}"
        return CheckResult("Fichiers communautaires", False, detail, weight=2)
    return CheckResult("Fichiers communautaires", True, detail, weight=2)


def check_tests(root: Path) -> CheckResult:
    for marker in TEST_MARKERS:
        path = root / marker
        if path.is_dir():
            test_files = list(path.rglob("test_*.py")) + list(path.rglob("*_test.py"))
            if test_files:
                return CheckResult(
                    "Tests",
                    True,
                    f"Répertoire {marker}/ avec {len(test_files)} fichier(s) de test",
                )
            return CheckResult(
                "Tests",
                False,
                f"Répertoire {marker}/ présent mais sans fichiers de test Python",
            )
    pyproject = root / "pyproject.toml"
    if pyproject.is_file() and "pytest" in pyproject.read_text(encoding="utf-8"):
        return CheckResult("Tests", False, "pytest déclaré mais aucun répertoire de tests trouvé")
    return CheckResult("Tests", False, "Aucun répertoire de tests détecté")


def check_workflows(root: Path) -> CheckResult:
    workflow_root = root / WORKFLOW_DIR
    if not workflow_root.is_dir():
        return CheckResult("GitHub Actions", False, "Dossier .github/workflows/ absent")
    workflows = [
        p for p in workflow_root.iterdir() if p.suffix in {".yml", ".yaml"} and p.is_file()
    ]
    if not workflows:
        return CheckResult("GitHub Actions", False, "Aucun workflow YAML trouvé")
    names = ", ".join(sorted(p.name for p in workflows))
    return CheckResult("GitHub Actions", True, f"Workflows: {names}")


def run_all_checks(root: Path) -> list[CheckResult]:
    """Exécute toutes les vérifications sur le dépôt local."""
    if not root.is_dir():
        raise FileNotFoundError(f"Chemin introuvable ou non-répertoire: {root}")
    return [
        check_readme(root),
        check_license(root),
        check_community_files(root),
        check_tests(root),
        check_workflows(root),
    ]


def score(results: list[CheckResult]) -> tuple[int, int]:
    """Retourne (points obtenus, points maximum)."""
    obtained = sum(r.weight for r in results if r.passed)
    maximum = sum(r.weight for r in results)
    return obtained, maximum

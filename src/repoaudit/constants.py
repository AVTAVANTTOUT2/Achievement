"""Constantes partagées par le moteur d'audit."""

from __future__ import annotations

EXIT_SUCCESS = 0
EXIT_STRICT_FAILURE = 1
EXIT_INVALID_PATH = 2

MIN_README_BYTES = 64

README_NAMES = ("README.md", "README.rst", "README.txt", "README")
LICENSE_NAMES = ("LICENSE", "LICENSE.md", "LICENSE.txt", "COPYING", "COPYING.md")
CONTRIBUTING_NAMES = ("CONTRIBUTING.md", "CONTRIBUTING", "docs/CONTRIBUTING.md")
CODE_OF_CONDUCT_NAMES = (
    "CODE_OF_CONDUCT.md",
    "CODE_OF_CONDUCT",
    ".github/CODE_OF_CONDUCT.md",
)
SECURITY_NAMES = ("SECURITY.md", ".github/SECURITY.md", "docs/SECURITY.md")
TEST_MARKERS = ("tests", "test", "spec", "__tests__")
WORKFLOW_DIR = ".github/workflows"

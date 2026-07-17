"""Point d'entrée CLI pour repoaudit."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from repoaudit import __version__
from repoaudit.checks import run_all_checks
from repoaudit.constants import EXIT_INVALID_PATH, EXIT_STRICT_FAILURE, EXIT_SUCCESS
from repoaudit.report import format_report


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="repoaudit",
        description="Audite la qualité communautaire d'un dépôt GitHub local.",
    )
    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Chemin du dépôt local à auditer (défaut: répertoire courant)",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Code de sortie 1 si le score est inférieur à 100%%",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    root = Path(args.path).expanduser().resolve()
    try:
        results = run_all_checks(root)
    except FileNotFoundError as exc:
        print(f"erreur: {exc}", file=sys.stderr)
        return EXIT_INVALID_PATH
    print(format_report(root, results))
    if args.strict and not all(r.passed for r in results):
        return EXIT_STRICT_FAILURE
    return EXIT_SUCCESS


if __name__ == "__main__":
    raise SystemExit(main())

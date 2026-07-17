#!/usr/bin/env bash
# Lint local du package repoaudit.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

if [[ -f .venv/bin/activate ]]; then
  # shellcheck disable=SC1091
  source .venv/bin/activate
fi

if ! command -v ruff >/dev/null 2>&1; then
  echo "ruff introuvable — installez les extras de développement : pip install -e '.[dev]'" >&2
  exit 127
fi

echo "→ ruff check src tests"
ruff check src tests

echo "→ ruff format --check src tests"
ruff format --check src tests

echo "Lint OK"

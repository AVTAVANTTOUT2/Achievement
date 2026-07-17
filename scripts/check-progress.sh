#!/usr/bin/env bash
# Affiche un état factuel du dépôt (pas les badges achievements GitHub).
set -euo pipefail

if ! command -v gh >/dev/null 2>&1; then
  echo "gh (GitHub CLI) est requis" >&2
  exit 127
fi

if ! command -v git >/dev/null 2>&1; then
  echo "git est requis" >&2
  exit 127
fi

REPO=$(gh repo view --json nameWithOwner -q .nameWithOwner)
OWNER=$(gh api user --jq .login)
PROFILE_URL="https://github.com/${OWNER}"
REPO_URL="https://github.com/${REPO}"

MERGED_PRS=$(gh pr list --repo "$REPO" --state merged --limit 100 --json number -q 'length')
COAUTHORED=$(gh api "repos/${REPO}/pulls?state=closed&per_page=100" --jq '[.[] | select(.merged_at != null) | select(.body // "" | test("Co-authored-by:"; "i") or (.title // "" | test("co-authored"; "i")))] | length' 2>/dev/null || echo "n/a")

# Fallback: scan merge commits for Co-authored-by trailers
COAUTHOR_COMMITS=$(git log --all --format='%B' | grep -c '^Co-authored-by: AVTAVANTTOUT2 ' || true)
COAUTHOR_ANY=$(git log --all --format='%B' | grep -c '^Co-authored-by:' || true)

STARS=$(gh api "repos/${REPO}" --jq .stargazers_count)
HAS_DISCUSSIONS=$(gh api "repos/${REPO}" --jq .has_discussions)
OPEN_ISSUES=$(gh issue list --repo "$REPO" --state open --limit 100 --json number -q 'length')
CLOSED_ISSUES=$(gh issue list --repo "$REPO" --state closed --limit 100 --json number -q 'length')

echo "=== repoaudit / Achievement — progression factuelle ==="
echo "Profil GitHub     : ${PROFILE_URL}"
echo "Dépôt             : ${REPO_URL}"
echo "PR fusionnées     : ${MERGED_PRS}"
echo "PR co-écrites (heuristique body/title) : ${COAUTHORED}"
echo "Commits Co-authored-by AVTAVANTTOUT2 : ${COAUTHOR_COMMITS}"
echo "Commits avec tout trailer Co-authored-by : ${COAUTHOR_ANY}"
echo "Étoiles           : ${STARS}"
echo "Discussions       : ${HAS_DISCUSSIONS}"
echo "Issues ouvertes   : ${OPEN_ISSUES}"
echo "Issues fermées    : ${CLOSED_ISSUES}"
echo
echo "Note: GitHub n'expose pas d'API officielle pour lire les achievements du profil."
echo "Ce script rapporte uniquement des métriques de dépôt vérifiables."

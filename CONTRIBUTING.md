# Guide de contribution

Merci de contribuer à **repoaudit**. Ce document décrit un flux simple et reproductible.

## Prérequis

- Python 3.10+
- Git
- Un fork ou un clone du dépôt

## Mise en place locale

```bash
git clone https://github.com/AVTAVANTTOUT2/Achievement.git
cd Achievement
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest -q
```

## Processus recommandé

1. Ouvrir une issue pour discuter du changement (sauf correctif trivial).
2. Créer une branche descriptive : `feat/...`, `fix/...`, `docs/...`.
3. Implémenter un changement **unique** et compréhensible.
4. Ajouter ou mettre à jour les tests.
5. Lancer `pytest -q` (et `ruff check src tests` si disponible).
6. Ouvrir une pull request avec un résumé clair et un plan de test.

## Standards de code

- Python typé, fonctions courtes, messages d'erreur actionnables.
- Pas de dépendances runtime supplémentaires sans discussion préalable.
- Pas de secrets, tokens ou données privées dans le dépôt.

## Messages de commit

Préférez des messages qui expliquent le *pourquoi* :

```text
Fix: accepter LICENSE.txt lors de la détection de licence.

Certains projets publient la licence sous LICENSE.txt ; l'audit doit les reconnaître.
```

## Revue

Une PR peut être fusionnée après vérification des tests. Les co-écritures réelles sont documentées dans `docs/PAIR_EXTRAORDINAIRE.md`.

## Code de conduite

Les interactions suivent le [Code of Conduct](CODE_OF_CONDUCT.md).

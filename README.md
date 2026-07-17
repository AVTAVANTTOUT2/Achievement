# Achievement — repoaudit

**repoaudit** est un outil en ligne de commande Python, sans dépendances runtime, qui audite la qualité communautaire d'un dépôt GitHub **local**.

Il répond à une question simple : *ce dépôt est-il prêt à accueillir des contributeurs ?*

## Proposition de valeur

Avant d'ouvrir un projet en open source — ou avant une revue interne — `repoaudit` contrôle en quelques secondes les signaux de maturité attendus par GitHub et la communauté :

- présence et densité minimale d'un README ;
- licence explicite ;
- fichiers communautaires (CONTRIBUTING, CODE_OF_CONDUCT, SECURITY) ;
- présence de tests automatisés ;
- workflows GitHub Actions.

Le résultat est un rapport terminal lisible, avec un score pondéré.

## Fonctionnalités

| Vérification | Ce qui est contrôlé |
| --- | --- |
| README | Fichier présent et suffisamment renseigné |
| Licence | `LICENSE` / `COPYING` détecté |
| Communauté | CONTRIBUTING, code de conduite, politique de sécurité |
| Tests | Répertoire de tests Python avec fichiers `test_*.py` |
| CI | Workflows YAML sous `.github/workflows/` |

## Installation

Prérequis : Python 3.10+.

```bash
git clone https://github.com/AVTAVANTTOUT2/Achievement.git
cd Achievement
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Usage

```bash
# Auditer le dépôt courant
python -m repoaudit .

# Équivalent via le script installé
repoaudit .

# Échec (exit 1) si le score n'est pas parfait
repoaudit --strict .

# Version
repoaudit --version
```

### Exemple de sortie

```text
repoaudit — rapport de qualité du dépôt
Cible : /chemin/vers/projet
────────────────────────────────────────────────
[✓] README: Présent: README.md (1200 octets)
[✓] Licence: Présent: LICENSE
[✗] Fichiers communautaires: Manquants: SECURITY
[✓] Tests: Répertoire tests/ avec 4 fichier(s) de test
[✓] GitHub Actions: Workflows: ci.yml
────────────────────────────────────────────────
Score : 4/6 (67%)
Statut : correct — quelques améliorations restantes.
```

## Démonstration

Depuis la racine de ce dépôt :

```bash
pytest -q
python -m repoaudit .
```

## Roadmap

- [ ] Sortie JSON (`--format json`) pour intégration CI
- [ ] Vérification des topics et de la description distante via `gh` (optionnelle)
- [ ] Règles configurables via `.repoaudit.toml`
- [ ] Support de marqueurs de tests non-Python

## Contribution

Les contributions sont les bienvenues. Voir [CONTRIBUTING.md](CONTRIBUTING.md).

Guide détaillé : [docs/USAGE.md](docs/USAGE.md)  
Suivi achievements : [ACHIEVEMENTS.md](ACHIEVEMENTS.md)

## Licence

Distribuée sous licence MIT — voir le fichier [LICENSE](LICENSE).

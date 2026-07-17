# Guide d'utilisation — repoaudit

Ce guide détaille l'usage quotidien de `repoaudit` au-delà du README.

## Installation

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
```

Vérifier l'installation :

```bash
repoaudit --version
python -m repoaudit --help
```

## Commandes

| Commande | Effet |
| --- | --- |
| `repoaudit` | Audite le répertoire courant |
| `repoaudit /chemin/projet` | Audite un chemin explicite |
| `repoaudit --strict .` | Exit code `1` si une vérification échoue |
| `repoaudit --version` | Affiche la version |

## Codes de sortie

| Code | Signification |
| --- | --- |
| `0` | Succès (rapport affiché) |
| `1` | Mode `--strict` : au moins une vérification a échoué |
| `2` | Chemin invalide ou introuvable |

## Interpréter le score

Le score est pondéré : les fichiers communautaires comptent double. Un dépôt peut donc afficher `5/6` même avec quatre checks verts.

Recommandation de progression :

1. README utile (≥ 64 octets)
2. LICENSE
3. CONTRIBUTING + CODE_OF_CONDUCT + SECURITY
4. Suite de tests
5. Workflow CI sous `.github/workflows/`

## Intégration CI

Exemple minimal (déjà fourni dans ce dépôt) :

```yaml
- run: pip install -e ".[dev]"
- run: pytest -q
- run: python -m repoaudit --strict .
```

Utilisez `--strict` uniquement lorsque vous voulez faire échouer le job CI sur un score incomplet.

## Dépannage

**`externally-managed-environment`**  
Créez un virtualenv ; n'installez pas le package dans le Python système Homebrew.

**Score bas malgré un README**  
Vérifiez la taille du fichier : un README trop court échoue volontairement.

**Workflows non détectés**  
Le dossier doit être `.github/workflows/` avec au moins un fichier `.yml` ou `.yaml`.

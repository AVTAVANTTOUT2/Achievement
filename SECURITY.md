# Politique de sécurité

## Versions supportées

| Version | Supportée |
| --- | --- |
| 1.0.x | Oui |
| 0.1.x | Oui (corrections de sécurité) |
| < 0.1 | Non |

## Signaler une vulnérabilité

Si vous découvrez une faille de sécurité dans `repoaudit` :

1. **Ne créez pas d'issue publique** décrivant l'exploit.
2. Utilisez les [GitHub Security Advisories](https://github.com/AVTAVANTTOUT2/Achievement/security/advisories/new) du dépôt.
3. Incluez : version concernée, étapes de reproduction, impact estimé, correctif proposé si disponible.

Nous accuserons réception sous **7 jours ouvrés** et proposerons un plan de correction ou d'atténuation.

## Périmètre

Ce projet est un outil d'audit local en lecture seule. Les risques typiques concernent :

- exécution sur des chemins utilisateur non validés ;
- fuites d'informations via des messages d'erreur ;
- dépendances de développement compromises.

## Bonnes pratiques pour les contributeurs

- Ne jamais committer de secrets, tokens ou fichiers `.env`.
- Préférer des messages d'erreur sans dump de données sensibles.
- Maintenir les dépendances de développement à jour.

# Pair Extraordinaire — collaboration réelle

Cet achievement exige une **vraie seconde personne**. Aucun commit n'est attribué artificiellement.

## Identité du co-auteur (compte propriétaire)

- Compte GitHub : `AVTAVANTTOUT2`
- Adresse co-auteur recommandée (noreply GitHub) :

```text
Co-authored-by: AVTAVANTTOUT2 <208137561+AVTAVANTTOUT2@users.noreply.github.com>
```

Alternative (forme courte) :

```text
Co-authored-by: AVTAVANTTOUT2 <AVTAVANTTOUT2@users.noreply.github.com>
```

Si vous préférez une adresse e-mail **vérifiée** sur GitHub, remplacez uniquement la partie entre `<...>`.  
**Ne jamais inventer une adresse.**

Placeholder si besoin de substitution manuelle :

```text
Co-authored-by: AVTAVANTTOUT2 <REMPLACER_PAR_EMAIL_VERIFIE_OU_NOREPLY>
```

## Issue de coordination

Ouvrir / utiliser l'issue intitulée **Pair Extraordinaire collaboration** pour convenir du changement et du binôme.

## Procédure pour un véritable collaborateur

1. **Forker** ou cloner le dépôt `https://github.com/AVTAVANTTOUT2/Achievement`.
2. Créer une branche descriptive, par exemple `pair/improve-json-flag`.
3. Travailler **réellement à deux** sur une petite amélioration (feature, docs, test).
4. Créer un commit où `AVTAVANTTOUT2` est **véritable co-auteur** (pair programming, revue active, ou contribution partagée), avec le trailer :

   ```bash
   git commit -m "$(cat <<'EOF'
   Feat: ajouter une option utile convenue ensemble.

   Co-authored-by: AVTAVANTTOUT2 <208137561+AVTAVANTTOUT2@users.noreply.github.com>
   EOF
   )"
   ```

5. Pousser la branche et ouvrir une pull request vers `main`.
6. Faire fusionner la PR (merge commit ou squash **en conservant** le trailer `Co-authored-by`).
7. Vérifier sur la PR fusionnée que le co-auteur apparaît bien.

## Checklist des seuils

| Niveau | PR co-écrites requises | État |
| --- | ---: | --- |
| Initial | 1 | À faire avec un vrai collaborateur |
| Bronze | 10 | Répéter le processus |
| Argent | 24 | Répéter le processus |
| Or | 48 | Répéter le processus |

## Ce qu'il ne faut pas faire

- Inventer un second compte
- Ajouter un trailer `Co-authored-by` pour quelqu'un qui n'a pas participé
- Réécrire l'historique publié pour injecter des co-auteurs

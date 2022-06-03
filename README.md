# Decklist Tutor

Ce script traduit les noms de cartes Magic The Gathering en anglais, afin de pouvoir facilement importer des listes de cartes d'un deck (decklists).

Fonctionne avec les sites suivants :

- www.deckstats.net

Cela n'a pas été testé sur d'autres plateformes. Si vous avez testé sur d'autres plateformes et que ça fonctionne (ou non), faites-le moi savoir !

## Installation et prérequis

Pour installer le script, Un simple `git-clone` suffira :

```bash
git clone https://github.com/lebarde/decklist-tutor
```

Pour fonctionner, il faut avoir installé Python3. Si jamais des dépendances ne sont pas satisfaites, vous pouvez les installer avec `pipreqs` :

```bash
pip install pipreqs
pipreqs .
```



## Usage

Sous linux, faire ceci :

```bash
$ ./mtg-translate.py chemin/de/votre/fichier-texte.txt
```


## Format du fichier texte

Votre fichier texte doit être composé de lignes comme ci-dessous.

```
N [CODE] Nom de la carte
```

- N est facultatif. C'est un nombre entier.
- [CODE] est facultatif. Il s'agit du code de l'extension. Par exemple, [SNC] est le code de l'extension des rues de la nouvelle Capenna
- Fichier de texte brut (pas de fichier tableur ni traitement de texte) ;
- Une carte unique par ligne (vous pouvez cependant noter qu'elle est en *n* exemplaires).

Exemple de fichier texte :

Mon-super-deck.txt
```
Adjudicateurs de Spara
Duelliste discipliné
Âme de l'émancipation
Régulatrice céleste
Animaux de compagnie exotiques
Journaleuse curieuse
[SNC] Évaluateur de cadavre
Buteur de corps
2 [SNC] Adepte des riveteurs
Évasion audacieuse
2 Grilleur de soirée fanfaron
Réserve scintillante
Ailes brisées
Pour la famille
Adepte des Cabaretti
```

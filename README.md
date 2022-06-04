# Decklist Tutor

Ce script utilise le service [Scryfall.com](https://www.scryfall.com) pour traduire les noms de cartes Magic The Gathering en anglais, afin de pouvoir facilement importer des listes de cartes d'un deck (decklists).

Fonctionne avec les sites suivants :

- www.deckstats.net

Cela n'a pas été testé sur d'autres plateformes. Si vous l'avez testé ailleurs, faites-le moi savoir !

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
$ ./decklist-tutor chemin/de/votre/fichier-texte.txt
```

Vous pouvez également ajouter ce script à votre variable `$PATH` pour pouvoir le lancer depuis n'importe où sans `./`.

## Format du fichier texte

Votre fichier texte doit être composé de lignes comme ci-dessous.

```
N [CODE] Nom de la carte
```

- `N` est facultatif. C'est un nombre entier.
- `[CODE]` est facultatif. Il s'agit du code de l'extension. Par exemple, `[SNC]` est le code de l'extension des rues de la nouvelle Capenna
- Fichier de texte brut (pas de fichier tableur ni traitement de texte) ;
- Une carte unique par ligne (vous pouvez cependant noter qu'elle est en *n* exemplaires).
- Vous pouvez écrire des commentaires. Une ligne de commentaire commence par un dièze `#`.

Exemple de fichier texte :

Mon-super-deck.txt
```
# Cartes draftées en New Capenna
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

Voici ce que donne Decklist tutor :

```
$ decklist-tutor Mon-super-deck.txt

=> Contenu du fichier Mon-super-deck_en.txt, qui vient d'être créé :

Spara's Adjudicators
Disciplined Duelist
Soul of Emancipation
Celestial Regulator
Exotic Pets
Snooping Newsie
[SNC] Corpse Appraiser
Body Dropper
2 [SNC] Riveteers Initiate
Daring Escape
2 Witty Roastmaster
Glittering Stockpile
Broken Wings
For the Family
Cabaretti Initiate
```

## Roadmap

- Créer une base de données TinySQL pour garder les recherches en mémoire.
- Créer des fichier exécutables autonomes sous Windows, Linux et IOS
- Application Android ?

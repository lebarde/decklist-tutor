#!/usr/bin/env python
import sys,requests, urllib, re, time, json, os

# define Python user-defined exceptions
class Error(Exception):
    """Base class for other exceptions"""
    pass
class CarteIntrouvable(Error):
    """Exception levée lorsqu'une carte est introuvable.

    Attributes:
        NomCarte -- Nom de la carte
        message -- explanation of the error
    """
    def __init__(self, NomCarte, message=""):
        self.NomCarte = NomCarte
        self.message = NomCarte + " : Carte introuvable."
        super().__init__(self.message)

    pass

def main(argv):
    NomFichierListe = argv[0]
    # Création d'un nouveau nom de fichier
    NomFichierTraduction = "{0}_{2}{1}".format(*os.path.splitext(NomFichierListe) + ("en",))
    
    # Using readlines()
    FichierListe = open(NomFichierListe, 'r')
    Cartes = FichierListe.readlines()
    
    FichierTraduction = open(NomFichierTraduction, 'a')
    
    count = 0
    countFound = 0
    cartesIntrouvables = []
    DateDernièreRecherche = current_milli_time()
    
    for Ligne in Cartes:
        count += 1
        Date = current_milli_time()
        NomCarte = StripLine(Ligne)
        NomCarteAnglaise = ""
        
        if (Date - DateDernièreRecherche < 70):
            time.sleep((Date - DateDernièreRecherche)/1000)
        DateDernièreRecherche = Date
        
        try:
            CarteTrouvée = RechercherCarte(NomCarte)
            NomCarteAnglaise = CarteTrouvée["name"]
            print(NomCarte + " => " + NomCarteAnglaise)
            NouvelleLigne = re.sub(r'[^0-9\[\]]+$', " " + NomCarteAnglaise, Ligne.strip())
            FichierTraduction.write(NouvelleLigne.strip() + "\n")
            countFound += 1
        except CarteIntrouvable as ex:
            #print(ex)
            cartesIntrouvables.append(NomCarte)
            # On écrit quand-même le nom en français dans le fichier !
            FichierTraduction.write(Ligne.strip() + "\n")
        
    print("\nNombre de cartes recherchées : " + str(count))
    print("Nombre de cartes trouvées : " + str(countFound))
    if len(cartesIntrouvables) > 0:
        print("Certaines cartes n'ont pas été trouvées :")
        print(*cartesIntrouvables, sep = "\n")
    
    # Ne pas oublier de fermer les fichiers ouverts
    FichierListe.close()
    FichierTraduction.close()
    return

def current_milli_time():
    return round(time.time() * 1000)

def StripLine(Ligne):
    # Le nom de la carte est formaté comme ceci :
    # N [EXT] Nom de la carte
    #   Où N est le nombre d'exemplaires,
    #   [EXT] est l'extension,
    #   suivis du nom réel de la carte.
    # Ici, on fait une substitution. On retire jusqu'à 5 chiffres à gauche,
    # puis jusqu'à 2 fois des suites de caractères entre crochets.
    #
    # Pour en savoir plus sur les rexex :
    #   cf. https://docs.python.org/fr/3/howto/regex.html
    # Allez, on respire un bon coup :
    LigneModifiée = re.sub(r'^(\d*){0,5}', '', Ligne.strip())
    LigneModifiée = re.sub(r'^(\[\w{3,5}\]){0,1}', '', LigneModifiée.strip())
    #print("Ligne modifiée : " + LigneModifiée)
    # Enfin, on retourne la chaîne de caractères sans les espaces.
    return(LigneModifiée.strip())

def RechercherCarte(NomCarte):
    # On encode le nom de la carte avec des pourcents
    # (cf. https://en.wikipedia.org/wiki/Percent-encoding)
    NomCarteEncodé = urllib.parse.quote(NomCarte.encode('utf8'))
    url = "https://api.scryfall.com/cards/named?lang=all&format=json&fuzzy=" + NomCarteEncodé
    réponse = requests.get(url)
    # Si la carte n'est pas trouvée ou qu'il y a eu un problème,
    # on envoie une exception.
    if réponse.status_code == 404:
        raise CarteIntrouvable(NomCarte)
    elif réponse.status_code != 200:
        réponse.raise_for_status()
    
    # On renvoie l'objet déserialisé en partant du format JSON.
    #print(reponse.json())
    return(réponse.json())

if __name__ == "__main__":
    main(sys.argv[1:])

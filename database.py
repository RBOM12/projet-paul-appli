import csv

def chercher_bdd_lunette_to_lentille(xl):
    with open('bdd lunette to lentille.csv') as fichier:
        lecteur = csv.reader(fichier,delimiter=';')
        for ligne in lecteur:
            if ligne[0] == xl:
                return ligne[1]
    return None



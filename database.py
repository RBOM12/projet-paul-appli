import csv

def chercher_bdd_lunette_to_lentille(xl):
    with open('bdd lunette to lentille.csv') as fichier:
        lecteur = csv.reader(fichier,delimiter=';')
        for ligne in lecteur:
            print(ligne)
            if ligne[0] == xl:
                print (ligne[1])
                return ligne[1]
    return None
x=float(chercher_bdd_lunette_to_lentille("-6"))*3
print(x)

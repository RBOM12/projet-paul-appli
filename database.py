import csv

from calculations import puissance_oeil


def chercher_bdd_lunette_to_lentille(xl):
    with open('bdd lunette to lentille.csv') as fichier:
        lecteur = csv.reader(fichier,delimiter=';')
        for ligne in lecteur:
            if ligne[0] == xl:
                return ligne[1]
    return None
puissance_oeil(9,-2,40)

def puissance_oeil(xl,yl,zl):
    #Transformation de la puissance lunette en lentille
    #utiliser la BDD pour le faire
    x_1=float(chercher_bdd_lunette_to_lentille(str(xl)))
    x_2=float(chercher_bdd_lunette_to_lentille(str(xl+yl)))
    xs=x_1
    ys=round(x_2-x_1,2)
    zs=zl
    print(xs," ; ",ys," ; ",zs)
    return xs,ys,zs

puissance_oeil(3.5,-3,40)
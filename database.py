import csv

def chercher_bdd_lunette_to_lentille(xl):
    with open('bdd lunette to lentille.csv') as fichier:
        lecteur = csv.reader(fichier,delimiter=';')
        for ligne in lecteur:
            if ligne[0] == xl:
                return ligne[1]
    return None



def chercher_aco (k,tor):
    with open('bdd k et tor.csv') as fichier:
        lecteur = csv.reader(fichier,delimiter=';')
        print(k,tor)
        for ligne in lecteur:
            ligne = [cell.replace(',', '.') for cell in ligne]
            if ligne[0] == k and ligne[1] == tor:
                return ligne[2]
    return None

def chercher_nf (k,tor):
    with open('bdd k et tor.csv') as fichier:
        lecteur = csv.reader(fichier,delimiter=';')
        for ligne in lecteur:
            ligne = [cell.replace(',', '.') for cell in ligne]
            if ligne[0] == k and ligne[1] == tor:
                return ligne[3]
    print("erreur sur nf")
    return None

def chercher_f (k,tor):
    with open('bdd k et tor.csv') as fichier:
        lecteur = csv.reader(fichier,delimiter=';')
        for ligne in lecteur:
            ligne = [cell.replace(',', '.') for cell in ligne]
            if ligne[0] == k and ligne[1] == tor:
                return ligne[4]
    print("erreur sur f")
    return None


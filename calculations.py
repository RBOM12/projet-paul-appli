from database import chercher_bdd_lunette_to_lentille, chercher_aco, chercher_nf, chercher_f
#cote est les coté choisi gauche = 0 et droit = 1
xl=[]
yl=[]
zl=[]
dhiv=0
diametre_pupille=0
recouvrement=0
k1=[]
x=[]
k2=[]
y=[]
excentricite=0


xs,ys,zs,tor,exi,r0,xdla,ydla,zdla,xlrpg,ylrpg,zlrpg,ai,nf,f,cptatr=[],[],[],0,0,0,0,0,0,0,0,0,0,0,0,0

def toricite(cote):
    #Calcul de la toricité
    global tor
    tor=round(k1[cote]-k2[cote],2)

def test_excentricite():
    #Test de l'excentricité si elle est supérieur à 0.55 ou inférieur à 0.45 et aura un impact sur R0
    global exi
    if excentricite<0.45:
        exi=-0.05
    elif 0.45 <= excentricite <= 0.55:
        exi=0
    else:
        exi=0.05
    return exi

def calculr0(cote):
    #Calcul de R0 en testant si tor sup ou inf a 0.2
    global r0
    if tor>0.2:
        r0=k1[cote]-(tor*1/3)+exi
    else:
        r0=k1[cote]+exi
    r0=round_to_plusproche_0_05(r0)
    return r0


def round_to_plusproche_0_05(number):
    return round(number * 20) / 20

def calcul_dla(cote):
    global xdla,ydla,zdla
    vdla1=(k1[cote]-r0)*5
    vdla2=(k2[cote]-r0)*5
    xdla=vdla1
    ydla=vdla2-vdla1
    zdla=zl
    return xdla,ydla,zdla

def calcul_dflrpg(cote):
    #Calcul de DFLRPG
    global xlrpg,ylrpg,zlrpg,xdla,ydla,zdla
    if zs != zdla:
        xdla = xdla - ydla
        ydla = -ydla

    #Calcul de DFLRGP
    xlrpg=xs[cote]-xdla
    ylrpg=ys[cote]-ydla
    zlrpg=zs
    return xlrpg,ylrpg,zlrpg
cpttranspo=0
def calcul_dflrpg2():
    #Transpo plus compteur de transpo
    global cpttranspo,xdla,ydla
    if -0.75 < ylrpg < 0:
        xdla=xdla+0.25
        ydla=0
        cpttranspo=1

def calcul_ai (cote) :
    # aller chercher dans la BDD
    global tor,xs,nf,f,ai
    aco = float(chercher_aco(str(k1[cote]),str(tor)))
    nf = float(chercher_nf(str(k1[cote]),str(tor)))
    f = float(chercher_f(str(k1[cote]),str(tor)))
    ai=xs[cote]-aco
    return ai,nf,f

def atr () :
    #calcul si c'est flex ou pas 1 flex 0 pas flex
    global nf,f,cptatr
    if nf>f :
        cptatr=1
    else:
        cptatr=0
    return cptatr


def submit_form(entries, cote):
    # Récupérer les données du formulaire
    data = {
        "xl": int(entries["XL"].get()),
        "yl": int(entries["YL"].get()),
        "zl": int(entries["ZL"].get()),
        "dhiv": int(entries["DHIV"].get()),
        "diametre_pupille": int(entries["Diamètre de la pupille"].get()),
        "recouvrement": int(entries["Recouvrement"].get()),
        "k1": float(entries["K1"].get()),
        "x": int(entries["X"].get()),
        "k2": float(entries["K2"].get()),
        "y": int(entries["Y"].get()),
        "excentricite": int(entries["Excentricité"].get()),
    }

    # Utilisation de variables globales pour stocker les données des deux yeux
    global xl, yl, zl, dhiv, diametre_pupille, recouvrement, k1, x, k2, y, excentricite

    # Mise à jour des listes pour chaque œil (gauche ou droit)
    # xl, yl, zl, k1, x, k2, y sont des listes, une pour chaque œil.
    # On utilise l'index `cote` pour mettre à jour l'œil correspondant (0 pour gauche, 1 pour droit).

    if len(xl) <= cote:
        xl.append(data["xl"])
    else:
        xl[cote] = data["xl"]

    if len(yl) <= cote:
        yl.append(data["yl"])
    else:
        yl[cote] = data["yl"]

    if len(zl) <= cote:
        zl.append(data["zl"])
    else:
        zl[cote] = data["zl"]

    if len(k1) <= cote:
        k1.append(data["k1"])
    else:
        k1[cote] = data["k1"]

    if len(x) <= cote:
        x.append(data["x"])
    else:
        x[cote] = data["x"]

    if len(k2) <= cote:
        k2.append(data["k2"])
    else:
        k2[cote] = data["k2"]

    if len(y) <= cote:
        y.append(data["y"])
    else:
        y[cote] = data["y"]

    # Les valeurs communes (non spécifiques à un œil)
    dhiv = data["dhiv"]
    diametre_pupille = data["diametre_pupille"]
    recouvrement = data["recouvrement"]
    excentricite = data["excentricite"]

    # Appeler la fonction calcul_total en passant l'œil actuel (cote)
    calcul_total(cote)


def puissance_oeil1(cote):
    #Transformation de la puissance lunette en lentille
    #utiliser la BDD pour le faire
    global xs,ys,zs
    print(str(xl))
    print(str(yl))
    s=xl[cote]+yl[cote]
    x_1=chercher_bdd_lunette_to_lentille(str(xl[cote]))
    x_2=chercher_bdd_lunette_to_lentille(str(s))
    xs.append(float(x_1))
    ys.append(float(x_2))
    zs=zl
    print(xs," ; ",ys," ; ",zs)

def calcul_total (cote):
    puissance_oeil1(cote)
    toricite(cote)
    test_excentricite()
    calculr0(cote)
    calcul_dla(cote)
    calcul_dflrpg(cote)
    calcul_ai(cote)
    atr()
    print(xl,yl,zl,dhiv,diametre_pupille,recouvrement,k1,x,k2,y,excentricite)
   # print(xs,ys,zs,tor,exi,r0,xdla,ydla,zdla,xlrpg,ylrpg,zlrpg,ai,nf,f,cptatr)
    return xs,ys,zs,tor,exi,r0,xdla,ydla,zdla,xlrpg,ylrpg,zlrpg,ai,nf,f,cptatr

def valeurxl(cote):
    return xl[cote]
def valeuryl():
    return yl
def valeurzl():
    return zl
def valeurdhiv():
    return dhiv
def valeurdiametre_pupille():
    return diametre_pupille
def valeurrecouvrement():
    return recouvrement
def valeurk1():
    return k1
def valeurx():
    return x
def valeurk2():
    return k2
def valeury():
    return y
def valeurexcentricite():
    return excentricite
def valeurxs():
    return xs
def valeurys():
    return ys
def valeurzs():
    return zs
def valeurtor():
    return tor
def valeurexi():
    return exi
def valeurr0():
    return r0
def valeurxdla():
    return xdla
def valeurydla():
    return ydla
def valeurzdla():
    return zdla
def valeurxlrpg():
    return xlrpg
def valeurylrpg():
    return ylrpg
def valeurzlrpg():
    return zlrpg
def valeurai():
    return ai
def valeurnf():
    return nf
def valeurf():
    return f

def valeurcptatr():
    return cptatr
def valeurcpttranspo():
    return cpttranspo

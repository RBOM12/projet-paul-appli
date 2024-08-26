from database import chercher_bdd_lunette_to_lentille, chercher_aco, chercher_nf, chercher_f
#cote est les coté choisi gauche = 0 et droit = 1
xl=[]
yl=[]
zl=[]
dhiv=[]
diametre_pupille=[]
recouvrement=[]
k1=[]
x=[]
k2=[]
y=[]
excentricite=[]
xs,ys,zs,tor,exi,r0,xdla,ydla,zdla,xlrpg,ylrpg,zlrpg,ai,nf,f,cptatr=[],[],[],[],[0,0],[],[],[],[],[],[],[],[0,0],[0,0],[0,0],[0,0]
cpttranspo=[0,0]
def toricite(cote):
    #Calcul de la toricité
    global tor
    if len(tor)<=cote:
        tor.append(round(k1[cote]-k2[cote],2))
    else:
        tor[cote]=round(k1[cote]-k2[cote],2)

def test_excentricite(cote):
    #Test de l'excentricité si elle est supérieur à 0.55 ou inférieur à 0.45 et aura un impact sur R0
    global exi
    if excentricite[cote]<  0.45:
        exi[cote]=-0.05
    elif 0.45 <= excentricite[cote] <= 0.55:
        exi[cote]=0
    else:
        exi[cote]=0.05

def calculr0(cote):
    #Calcul de R0 en testant si tor sup ou inf a 0.2
    global r0
    if tor[cote]>0.2:
        r0=k1[cote]-(tor[cote]*1/3)+exi[cote]
    else:
        r0=k1[cote]+exi[cote]
    r0=round_to_plusproche_0_05(r0)
    r1=round_to_plusproche_0_05(r0)
    print("R0 =" + str(r0) + "R1 =" + str(r1))
    return r0


def round_to_plusproche_0_05(number):
    return round(number / 0.05) * 0.05

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
    if len(xlrpg) <= cote:
        xlrpg.append(xs[cote] - xdla)
    else:
        xlrpg[cote] = xs[cote] - xdla

    if len(ylrpg) <= cote:
        ylrpg.append(ys[cote] - ydla)
    else:
        ylrpg[cote] = ys[cote] - ydla

    if len(zlrpg) <= cote:
        zlrpg.append(zs)
    else:
        zlrpg[cote] = zs

    return xlrpg[cote],ylrpg[cote],zlrpg[cote]

def calcul_dflrpg2(cote):
    #Transpo plus compteur de transpo

    global cpttranspo,xdla,ydla
    if -0.75 < ylrpg[cote] < 0:
        xdla[cote]=xdla[cote]+0.25
        ydla[cote]=0

        cpttranspo[cote] = 1


def calcul_ai (cote) :
    # aller chercher dans la BDD
    global tor,xs,nf,f,ai
    aco=[0,0]
    aco[cote] = float(chercher_aco(str(k1[cote]),str(tor[cote])))
    nf[cote] = float(chercher_nf(str(k1[cote]),str(tor[cote])))
    f[cote] = float(chercher_f(str(k1[cote]),str(tor[cote])))
    ai=xs[cote]-aco[cote]


def atr (cote) :
    #calcul si c'est flex ou pas 1 flex 0 pas flex
    global nf,f,cptatr
    if nf[cote]>f[cote] :
        cptatr[cote]=1
    else:
        cptatr[cote]=0



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
        "excentricite": float(entries["Excentricité"].get()),
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
    if len(excentricite) <= cote:
        excentricite.append(data["excentricite"])
    else:
        excentricite[cote] = data["excentricite"]

    if len(dhiv) <= cote:
        dhiv.append(data["dhiv"])
    else:
        dhiv[cote] = data["dhiv"]

    if len(diametre_pupille) <= cote:
        diametre_pupille.append(data["diametre_pupille"])
    else:
        diametre_pupille[cote] = data["diametre_pupille"]

    if len(recouvrement) <= cote:
        recouvrement.append(data["recouvrement"])
    else:
        recouvrement[cote] = data["recouvrement"]


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
    test_excentricite(cote)
    calculr0(cote)
    calcul_dla(cote)
    calcul_dflrpg(cote)
    calcul_ai(cote)
    atr(cote)
    print(xl,yl,zl,dhiv,diametre_pupille,recouvrement,k1,x,k2,y,excentricite)
   # print(xs,ys,zs,tor,exi,r0,xdla,ydla,zdla,xlrpg,ylrpg,zlrpg,ai,nf,f,cptatr)
    return xs,ys,zs,tor,exi,r0,xdla,ydla,zdla,xlrpg,ylrpg,zlrpg,ai,nf,f,cptatr

def reset ():
    global xl,yl,zl,dhiv,diametre_pupille,recouvrement,k1,x,k2,y,excentricite
    xl=[]
    yl=[]
    zl=[]
    dhiv=[]
    diametre_pupille=[]
    recouvrement=[]
    k1=[]
    x=[]
    k2=[]
    y=[]
    excentricite=0
    global xs,ys,zs,tor,exi,r0,xdla,ydla,zdla,xlrpg,ylrpg,zlrpg,ai,nf,f,cptatr
    xs,ys,zs,tor,exi,r0,xdla,ydla,zdla,xlrpg,ylrpg,zlrpg,ai,nf,f,cptatr=[],[],[],[],[0,0],[],[],[],[],[],[],[],[0,0],[0,0],[0,0],[0,0]
    global cpttranspo
    cpttranspo=[0,0]

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

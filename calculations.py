
from database import chercher_bdd_lunette_to_lentille, chercher_aco, chercher_nf, chercher_f
from gestion_pdf import lien_pdf

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
xs,ys,zs,tor,exi,r0,xdla,ydla,zdla,xlrpg,ylrpg,zlrpg,ai,nf,f,cptatr=[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]
cpttranspo=[0,0]
PSC=[0,0]
tonus=[0,0]
HPL=[0,0]#Hauteur du prisme de larme
GL=[0,0]#Grade lipide
CL=[0,0]#charge lacrymale

gauche = 0
droit = 1
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
def dhivcalc (cote):
    if abs(xl[cote])+abs(yl[cote])<=6:
        dhiv[cote] = dhiv[cote] - 2.5
        return
    if tonus == 2:
        dhiv[cote]=dhiv[cote]-2.5
    elif tonus == 0:
        dhiv[cote]=dhiv[cote]-2.0
    else:
        distance1=abs(9.4-dhiv[cote]-2.5)
        distance2=abs(9.4-dhiv[cote]-2.0)
        if distance1<distance2:
            dhiv[cote]=dhiv[cote]-2.5
        else:
            dhiv[cote]-2.0

def calculr0(cote):
    #Calcul de R0 en testant si tor sup ou inf a 0.2

    if tor[cote]>0.2:
        r0[cote]=k1[cote]-(tor[cote]*1/3)+exi[cote]
    else:
        r0[cote]=k1[cote]+exi[cote]
    r0[cote]=round_to_plusproche_0_05(r0[cote])

    print("R0 =" + str(r0[cote]) )


def round_to_plusproche_0_05(number):
    return round(number / 0.05) * 0.05

def calcul_dla(cote):
    global xdla,ydla,zdla
    vdla1=(k1[cote]-r0[cote])*5
    vdla2=(k2[cote]-r0[cote])*5
    xdla[cote]=vdla1
    ydla[cote]=vdla2-vdla1
    zdla[cote]=zl[cote]
    return xdla,ydla,zdla

def calcul_dflrpg(cote):
    #Calcul de DFLRPG
    global xlrpg,ylrpg,zlrpg,xdla,ydla,zdla

   # if zs != zdla:
    #    xdla = xdla - ydla
     #   ydla = -ydla

    #Calcul de DFLRGP
    if len(xlrpg) <= cote:
        xlrpg.append(round(xs[cote] - xdla[cote],1))
    else:
        xlrpg[cote] = round(xs[cote] - xdla[cote],1)

    if len(ylrpg) <= cote:
        ylrpg.append(round(ys[cote] - ydla[cote],1))
    else:
        ylrpg[cote] = round(ys[cote] - ydla[cote])

    if len(zlrpg) <= cote:
        zlrpg.append(zs[cote])
    else:
        zlrpg[cote] = zs[cote]

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
    global tor,ys,nf,f,ai
    aco=[0,0]
    aco[cote] = float(chercher_aco(str(k1[cote]),str(tor[cote])))
    nf[cote] = float(chercher_nf(str(k1[cote]),str(tor[cote])))
    f[cote] = float(chercher_f(str(k1[cote]),str(tor[cote])))
    ai[cote]=ys[cote]-aco[cote]


def atr (cote) :
    #calcul si c'est flex ou pas 1 flex 0 pas flex
    global nf,f,cptatr,ai
    if HPL[cote] == 2:
        cptatr[cote]=1
        return
    elif HPL[cote] == 0:
        cptatr[cote]=0
        return
    else:
        if float(abs(abs(ai[cote] + nf[cote]) - abs(ai[cote] + f[cote]))) <= 0.1 and GL[cote] == 2:
            cptatr[cote]=0
        elif float(abs(abs(ai[cote] + nf[cote]) - abs(ai[cote] + f[cote]))) <= 0.1 and CL[cote] == 2:
            cptatr[cote]=1
        elif abs(ai[cote]+nf[cote])>abs(ai[cote]+f[cote]) :
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

def submit_form_deroulant(entries, cote):
    # Récupérer les données du formulaire
    option_values_gl_cl={"faible":0,"standard":1,"élevée":2}
    option_values_hpl={"0.2 <":0,"0.2 < X < 0.4":1," 0.40 <":2}
    option_values_psc={"lent":0, "standard":1,"rapide":2 }

    data = {
        "PSC":  option_values_psc[entries["PSC"].get()],
        "Tonus": option_values_gl_cl[entries["Tonus"].get()],
        "HPL": option_values_hpl[entries["HPL"].get()],
        "GL": option_values_gl_cl[entries["GL"].get()],
        "CL": option_values_gl_cl[entries["CL"].get()],
    }

    # Utilisation de variables globales pour stocker les données des deux yeux
    global PSC, tonus, HPL, GL, CL

    # Mise à jour des listes pour chaque œil (gauche ou droit)
    # xl, yl, zl, k1, x, k2, y sont des listes, une pour chaque œil.
    # On utilise l'index `cote` pour mettre à jour l'œil correspondant (0 pour gauche, 1 pour droit).

    if len(PSC) <= cote:
        PSC.append(data["PSC"])
    else:
        PSC[cote] = data["PSC"]

    if len(tonus) <= cote:
        tonus.append(data["Tonus"])
    else:
        tonus[cote] = data["Tonus"]

    if len(HPL) <= cote:
        HPL.append(data["HPL"])
    else:
        HPL[cote] = data["HPL"]

    if len(GL) <= cote:
        GL.append(data["GL"])
    else:
        GL[cote] = data["GL"]

    if len(CL) <= cote:
        CL.append(data["CL"])
    else:
        CL[cote] = data["CL"]



def puissance_oeil1(cote):
    #Transformation de la puissance lunette en lentille
    #utiliser la BDD pour le faire
    global xs,ys,zs
    print(str(xl))
    print(str(yl))
    s=xl[cote]+yl[cote]
    x_1=chercher_bdd_lunette_to_lentille(str(xl[cote]))
    x_2=chercher_bdd_lunette_to_lentille(str(s))
    if len(xs) <= cote:
        xs.append(float(x_1))
    else:
        xs[cote] = float(x_1)
    if len(ys) <= cote:
        ys.append(float(x_2))
    else:
        ys[cote] = float(x_2)

    zs=zl
    print(xs," ; ",ys," ; ",zs)

def calcul_total (cote):
    puissance_oeil1(cote)
    toricite(cote)
    dhivcalc(cote)
    test_excentricite(cote)
    calculr0(cote)
    calcul_dla(cote)
    calcul_dflrpg(cote)
    calcul_ai(cote)
    atr(cote)
    print( "XL",xl ,yl,zl,dhiv,diametre_pupille,recouvrement,k1,x,k2,y,excentricite)
    print("XS",xs,ys,zs,tor,exi,r0,xdla,ydla,zdla,xlrpg,ylrpg,zlrpg,ai,nf,f,cptatr)
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
def valeuryl(cote):
    return yl[cote]
def valeurzl(cote):
    return zl[cote]
def valeurdhiv(cote):
    return dhiv[cote]
def valeurdiametre_pupille(cote):
    return diametre_pupille[cote]
def valeurrecouvrement(cote):
    return recouvrement[cote]
def valeurk1(cote):
    return k1[cote]
def valeurx(cote):
    return x[cote]
def valeurk2(cote):
    return k2[cote]
def valeury(cote):
    return y[cote]
def valeurexcentricite(cote):
    return excentricite[cote]
def valeurxs(cote):
    return xs[cote]
def valeurys(cote):
    return ys[cote]
def valeurzs(cote):
    return zs[cote]
def valeurtor(cote):
    return tor[cote]
def valeurexi(cote):
    return exi[cote]
def valeurr0(cote):
    return r0[cote]
def valeurxdla(cote):
    return xdla[cote]
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

datag = {
        "xs gauche": valeurxs(0),
        "xs droit": valeurxs(1),
    }
datad = {
        "xs gauche": valeurxs(0),
        "xs droit": valeurxs(1),
    }
info = {"Nom": "Dupont", "Prénom": "Jean", "Âge": 29}
lentille = "souple"



def valeurpdf (infocomp):
    infocomp=infocomp.get()
    option_values_hpl_inverse = {0: "0.2 <", 1: "0.2 < X < 0.4", 2: " 0.40 <"}
    option_values_psc_inverse = {0: "lent", 1: "standard", 2: "rapide"}
    option_values_gl_cl_inverse = {0: "faible", 1: "standard", 2: "élevée"}
    lien_pdf(datag, datad, info, lentille, option_values_psc_inverse[PSC[gauche]], option_values_psc_inverse[PSC[droit]],  option_values_gl_cl_inverse[tonus[gauche]],  option_values_gl_cl_inverse[tonus[droit]], option_values_hpl_inverse[HPL[gauche]], option_values_hpl_inverse[HPL[droit]], option_values_gl_cl_inverse[GL[gauche]], option_values_gl_cl_inverse[GL[droit]], option_values_gl_cl_inverse[CL[gauche]], option_values_gl_cl_inverse[CL[droit]], infocomp, dhiv[0],dhiv[1],r0[0],r0[1],xlrpg[0],xlrpg[1],ylrpg[0],ylrpg[1],zlrpg[0],zlrpg[1],"SA")

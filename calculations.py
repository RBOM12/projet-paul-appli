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
def submit_form(entries,cote):
    data = {
        "xl": entries["XL"].get(),
        "yl": entries["YL"].get(),
        "zl": entries["ZL"].get(),
        "dhiv": entries["DHIV"].get(),
        "diametre_pupille": entries["diametre_pupille"].get(),
        "recouvrement": entries["recouvrement"].get(),
        "k1": entries["K1"].get(),
        "x": entries["X"].get(),
        "k2": entries["K2"].get(),
        "y": entries["Y"].get(),
        "excentricite": entries["Excentricité"].get(),
    }
    global xl, yl, zl, dhiv, diametre_pupille, recouvrement, k1, x, k2, y, excentricite
    if len(xl) == 0 or len (xl) == 1:
        print(len(xl))
        xl.append(int(data["xl"]))
    else:
        xl[cote]=int(data["xl"])

    if len(yl) == 0 or len(yl) == 1:
        yl.append(int(data["yl"]))
    else:
        yl[cote]=int(data["yl"])

    if len(zl) == 0 or len(zl) == 1:
        zl.append(int(data["zl"]))
    else:
        zl[cote]=int(data["zl"])

    dhiv = int(data["dhiv"])

    diametre_pupille = int(data["diametre_pupille"])

    recouvrement = int(data["recouvrement"])

    if len(k1) == 0 or len(k1) == 1:
        k1.append(float(data["k1"]))
    else:
        k1[cote]=float(data["k1"])
    if len(x) == 0 or len(x) == 1:
        x.append(int(data["x"]))
    else:
        x[cote]=int(data["x"])
    if len (k2) == 0 or len(k2) == 1:
        k2.append(float(data["k2"]))
    else:
        k2[cote]=float(data["k2"])
    if len(y) == 0 or len(y) == 1:
        y.append(int(data["y"]))
    else:
        y[cote]=int(data["y"])

    excentricite = int(data["excentricite"])


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

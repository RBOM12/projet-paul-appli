from database import  chercher_bdd_lunette_to_lentille

xl=0
yl=0
zl=0
dhiv=0
diametre_pupille=0
recouvrement=0
k1=0
x=0
k2=0
y=0
excentricite=0

xs,ys,zs,tor,exi,r0,xdla,ydla,zdla,xlrpg,ylrpg,zlrpg,ai,nf,f,cptatr=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

def toricite():
    #Calcul de la toricité
    global tor
    tor=k2-k1

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

def calculr0():
    #Calcul de R0 en testant si tor sup ou inf a 0.2
    global r0
    if tor>0.2:
        r0=k1-(tor*1/3)+exi
    else:
        r0=k1+exi
    r0=round_to_plusproche_0_05(r0)
    return r0


def round_to_plusproche_0_05(number):
    return round(number * 20) / 20

def calcul_dla():
    global xdla,ydla,zdla
    vdla1=(k1-r0)*5
    vdla2=(k2-r0)*5
    xdla=vdla1
    ydla=vdla2-vdla1
    zdla=zl
    return xdla,ydla,zdla

def calcul_dflrpg():
    #Calcul de DFLRPG
    global xlrpg,ylrpg,zlrpg,xdla,ydla,zdla
    if zs != zdla:
        xdla = xdla - ydla
        ydla = -ydla

    #Calcul de DFLRGP
    xlrpg=xs-xdla
    ylrpg=ys-ydla
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

def calcul_ai () :
    # aller chercher dans la BDD
    global tor,xs,nf,f,ai
    aco=1 #k1,tor
    nf =0.1 #k1,tor
    f=0.3 #k1,tor
    ai=xs-aco
    return ai,nf,f

def atr () :
    #calcul si c'est flex ou pas 1 flex 0 pas flex
    global nf,f,cptatr
    if nf>f :
        cptatr=1
    else:
        cptatr=0
    return cptatr
def submit_form(entries):
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
    xl = int(data["xl"])
    yl = int(data["yl"])
    zl = int(data["zl"])
    dhiv = int(data["dhiv"])
    diametre_pupille = int(data["diametre_pupille"])
    recouvrement = int(data["recouvrement"])
    k1 = int(data["k1"])
    x = int(data["x"])
    k2 = int(data["k2"])
    y = int(data["y"])
    excentricite = int(data["excentricite"])


    calcul_total()

def puissance_oeil1():
    #Transformation de la puissance lunette en lentille
    #utiliser la BDD pour le faire
    global xs,ys,zs
    x_1=float(chercher_bdd_lunette_to_lentille(str(xl)))
    x_2=float(chercher_bdd_lunette_to_lentille(str(xl+yl)))
    xs=x_1
    ys=round(x_2-x_1,2)
    zs=zl
    print(xs," ; ",ys," ; ",zs)

def calcul_total ():
    puissance_oeil1()
    toricite()
    test_excentricite()
    calculr0()
    calcul_dla()
    calcul_dflrpg()
    calcul_ai()
    atr()
    print(xs,ys,zs,tor,exi,r0,xdla,ydla,zdla,xlrpg,ylrpg,zlrpg,ai,nf,f,cptatr)
    return xs,ys,zs,tor,exi,r0,xdla,ydla,zdla,xlrpg,ylrpg,zlrpg,ai,nf,f,cptatr

def valeurxl():
    return xl
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

from ast import increment_lineno


xs,ys,zs,tor,exi,r0,xdla,ydla,zdla,xlrpg,ylrpg,zlrpg,ai,nf,f,cptatr=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

def puissance_oeil():
    #Transformation de la puissance lunette en lentille
    #utiliser la BDD pour le faire
    global xs,ys,zs
    x_1=xl
    x_2=yl+xl
    xs=x_1
    ys=x_2
    zs=zl

    return xs,ys,zs

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
    global xl,yl,zl,dhiv,diametre_pupille,recouvrement,k1,x,k2,y,excentricite
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
    print(data) # Vous pouvez remplacer cela par toute autre action à effectuer avec les données

def calcul_total ():
    puissance_oeil()
    toricite()
    test_excentricite()
    calculr0()
    calcul_dla()
    calcul_dflrpg()
    calcul_ai()
    atr()
    print(xs,ys,zs,tor,exi,r0,xdla,ydla,zdla,xlrpg,ylrpg,zlrpg,ai,nf,f,cptatr)
    return xs,ys,zs,tor,exi,r0,xdla,ydla,zdla,xlrpg,ylrpg,zlrpg,ai,nf,f,cptatr


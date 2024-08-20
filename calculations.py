def puissance_oeil(xl,yl,zl):
    #Transformation de la puissance lunette en lentille
    #utiliser la BDD pour le faire
    x_1=xl
    x_2=yl+xl
    xs=x_1
    ys=x_2
    zs=zl

    return xs,ys,zs

def toricité(k1,k2):
    #Calcul de la toricité
    tor: int=k2-k1
    return tor

def test_excentricité(excentricite):
    #Test de l'excentricité si elle est supérieur à 0.55 ou inférieur à 0.45 et aura un impact sur R0
    if excentricite<0.45:
        exi=-0.05
    elif 0.45 <= excentricite <= 0.55:
        exi=0
    else:
        exi=0.05
    return exi

def calculr0(k1,tor,exi):
    #Calcul de R0 en testant si tor sup ou inf a 0.2
    if tor>0.2:
        r0=k1-(tor*1/3)+exi
    else:
        r0=k1+exi
    r0=round_to_plusproche_0_05(r0)
    return r0


def round_to_plusproche_0_05(number):
    return round(number * 20) / 20

def calcul_dla(k1,k2,r0,zl):
    vdla1=(k1-r0)*5
    vdla2=(k2-r0)*5
    xdla=vdla1
    ydla=vdla2-vdla1
    zdla=zl
    return xdla,ydla,zdla

def calcul_dflrpg(xs,xdla,ydla,zs,zdla,ys):
    #Calcul de DFLRGP
    xlrpg=xs-xdla
    ylrpg=ys-ydla
    zlrpg=zs

    if zs!=zdla:
        xdla=xdla-ydla
        ydla=-ydla



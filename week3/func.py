import numpy as np

"""
Dit script is een verzameling van functies die overal in het dossier terugkomen, op deze manier hoeven ze niet telkens
verklaard te worden en zijn ze makkelijk centraal bereikbaar.

"""

def Indices(n:int):
    """
        Geeft een rij integers van -n tot n terug, om symmetrieën om de y-as mooi mee weer te kunnen geven.
    """
    return np.arange(-n, n)

def Step(n, n0=0):
    """
        Neemt een array van integers aan.
        Geeft 1 wanneer n >= n0 (n0 is standaard 0), en 0 wanneer n < n0. In andere woorden: de step-functie.
    """
    out = []

    for i in n:
        if ((i - n0) >= 0):
            out.append(1)
        else:
            out.append(0)

    return out


def DiscStep(n:int):
    """
        Een variant op de step-functie die een enkele integer inneemt als parameter in plaats van een array aan integers.
    """ 
    if n >= 0 :
        return 1
    else:
        return 0

def Delta(n, n0=0):
    """
        De diracdelta-functie, geeft 1 op n0 (n0 is standaard 0), en 0 op alle andere waarden voor n.
        Neemt een array van integers in.
    """
    out = []

    for i in n:
        if ((i-n0) == 0):
            out.append(1)
        else:
            out.append(0)
        
    return out
    
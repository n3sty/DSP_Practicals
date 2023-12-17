import numpy as np


def Indices(n):
    return np.arange(-n , n)

def Step(n, n0=0):
    
    out = []

    for i in n:
        if ((i - n0) >= 0):
            out.append(1)
        else:
            out.append(0)

    return out


def DiscStep(n):
    if n >= 0 :
        return 1
    else:
        return 0

def Delta(n, n0=0):

    out = []

    for i in n:
        if ((i-n0) == 0):
            out.append(1)
        else:
            out.append(0)
        
    return out
    
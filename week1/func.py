import numpy as np


def Indices(n):
    return np.arange(-n , n + 1)


def Step(n, n0=0):
    
    out = []

    for i in n:
        if ((i - n0) >= 0):
            out.append(1)
        else:
            out.append(0)

    return out


def Delta(n, n0=0):

    out = []

    for i in n:
        if ((i-n0) == 0):
            out.append(1)
        else:
            out.append(0)
        
    return out
    
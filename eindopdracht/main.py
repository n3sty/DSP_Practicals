"""
    Eindopdracht van DSP
    
    -Beschrijving:
        Van een gegeven signaal van 20.000 samples (f_s = 5000 Hz)
    
    -Datum:
        19 December 2023
    -Auteurs:
        RWW Lamain & J Siemerink
"""

import scipy.io
import matplotlib.pyplot as plt
from signalClass import Signal

mat = {}
scipy.io.loadmat("eindopdracht/signaal", mat, appendmat=True)

sig = Signal("Unfiltered Signal")

plt.figure(sig.title)
plt.title(sig.title)
plt.plot(sig.x, sig.y)
plt.show()
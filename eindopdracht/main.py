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
import numpy as np
import matplotlib.pyplot as plt
from signalGenerator import Signal
import DFT

# Declaring variables
PI = np.pi

sig = Signal(freq=(2*PI)/(50), sample_f=(50)/(2*PI), order=4)
sin = sig.constructSignal("sine")

plt.figure("Naked Signal")
plt.plot(sig.samples, sin)


y = np.fft.fft(sin)
x = np.fft.fftfreq(y.size, (2*PI)/(50))


plt.figure("FFT")
plt.stem(x/PI, abs(y))
plt.xlim(-1, 1)
plt.show()

# mat = {}
# scipy.io.loadmat("eindopdracht/signaal", mat, appendmat=True)

# sig = Signal("Unfiltered Signal", 'signaal.mat')
# sig.plot()
# plt.show()
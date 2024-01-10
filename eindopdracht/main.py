"""
    Eindopdracht van DSP
    
    -Beschrijving:
        Van een gegeven signaal van 20.000 samples (f_s = 5000 Hz)
    
    -Datum:
        19 December 2023
    -Auteurs:
        RWW Lamain & J Siemerink
"""

import numpy as np
import matplotlib.pyplot as plt
from signalGenerator import Signal

# Declaring variables
PI = np.pi                      
f = 1                         
s = 100                          
samples = int(2*s/f)            

# Generating a signal
sig = Signal(f, samples, order=2, phase=0)
sin = sig.constructSignal("sine")

# Noise
# sin = sin + np.random.normal(0, 0.1, len(sin))

# Plotting the signal
plt.figure("Naked Signal")
plt.subplot(1, 2, 1)
plt.grid(True)
plt.plot(sig.samples, sin)

# Plotting the FFT
y = np.fft.fft(sin) / len(sin)
x = np.fft.fftfreq(sig.samples.size, 1/sig.f)

# x = np.fft.fftfreq(y.size, 1/f)

plt.subplot(1, 2, 2)
plt.stem(x, abs(y))
plt.grid(True, which="both")
plt.show()

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
import signalGenerator 
import signalClass

# Declaring variables
PI = np.pi                      
f = 1                         
s = 100                          
samples = int(2*s/f)            

def SigFFT(yData):
    
    yData = yData[:500]
    xData = np.arange(len(yData))
    
    plt.figure("Signal")
    plt.plot(xData, yData)

    yFFT = np.fft.fft(yData) / len(yData)
    xF = np.fft.fftfreq(len(yData), 10)


    plt.figure("FFT")
    plt.stem(xF, np.abs(yFFT))
    # plt.xlim(-1, 1)
    plt.show()

# sig = signalClass.Signal()
sig = signalGenerator.Signal(freq=1/10, sample_f=1, order=1)

SigFFT(sig.y)

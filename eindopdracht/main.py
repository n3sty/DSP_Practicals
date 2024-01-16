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
import os
import scipy.io
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# Declaring variables
PI = np.pi
sampleFreq = 5000 # Hz
N = 4 * sampleFreq # 1/2 periods times sample frequency = number of samples
freq = 20 # Hz
gs = gridspec.GridSpec(2, 2)


def constructSignal(type, order, phase=0):
        # Generate signal
        print("Generating signal...")
        time = np.arange(N) / sampleFreq
        sig = np.zeros(N)
        
        if type == "sine":
            for i in range(1, order + 1):
                sine = 1/i * np.sin(freq*i*2*PI*time + phase)
                sign = -1 if i % 2 == 0 else 1
                sig = sig + sine * sign
            sig = sig * np.sin(2*PI*time)
            print("Signal generated")
            return sig


def SigFFT(yData, title, window=False):
    print("Calculating FFT...")
    # Generate signal
    time = np.arange(N) / sampleFreq
    signal = TriangleWindow(yData) if window else yData
    fftSignal = np.fft.fftshift(np.fft.fft(signal) / len(signal))
    magSignal = np.abs(fftSignal)
    phiSignal = np.angle(fftSignal)
    print("FFT calculated")
    # Generate frequency axis
    freqAxis = np.fft.fftshift(np.fft.fftfreq(len(signal), 1/sampleFreq))
    
    print(len(magSignal))
    
    print("Plotting...")
    # Plot signal
    plt.figure(title)
    plt.subplot(gs[0, :])
    plt.plot(time, signal, '-', linewidth=0.5)
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.title("Signal")
    plt.grid(True)
    
    # Plot FFT
    plt.subplot(gs[1, 0])
    plt.stem(freqAxis, magSignal)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.title("FFT")
    plt.grid(True)
    
    # Plot phase
    plt.subplot(gs[1, 1])
    plt.stem(freqAxis, phiSignal)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Phase (rad)")
    plt.title("Phase")
    plt.grid(True)
    
    print("Plots generated")
    
    plt.tight_layout()  # Add this line to adjust the spacing between subplots


def TriangleWindow(sig):
    # Generate window
    window = np.zeros(N)
    window[0:int(N/2)] = np.arange(0, 1, 1/int(N/2))
    window[int(N/2):N] = np.arange(1, 0, -1/int(N/2))
        
    # Apply window
    sig = sig * window
    
    print("Window applied")
        
    return sig

sig = np.reshape(scipy.io.loadmat(f'{os.path.dirname(os.path.realpath(__file__))}/{"signaal.mat"}')['sig'], 20000)
# sig = constructSignal("sine", 5, 0.1)

# SigFFT(sig, "Windowed",True)
SigFFT(sig, "Raw", False)

plt.show()

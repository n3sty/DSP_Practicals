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
import matplotlib.gridspec as gridspec
import signalClass

# Declaring variables
PI = np.pi
sampleFreq = 5000 # Hz
N = 20000 # Samples
freq = 1/2 # Hz
gs = gridspec.GridSpec(2, 2)
f_max = sampleFreq/2 # Hz


def constructSignal(type, order, phase=0):
        # Generate signal
        print("Generating signal...")
        sig = np.zeros(N)
        time = np.arange(N) / sampleFreq
        
        if type == "sine":
            for i in range(1, order + 1):
                sine = 1/i * np.sin(freq*i*2*PI*time + phase)
                sig = sig + sine
            # sig = sig * 0.5 * np.sin(1/100 * self.samples)
            print("Signal generated")
            return sig


def SigFFT(yData):
    print("Calculating FFT...")
    # Generate signal
    time = np.arange(N) / sampleFreq
    signal = TriangleWindow(yData)
    fftSignal = np.fft.fftshift(np.fft.fft(signal) / len(signal))
    magSignal = np.abs(fftSignal)
    phiSignal = np.angle(fftSignal)
    print("FFT calculated")
    # Generate frequency axis
    freqAxis = np.fft.fftshift(np.fft.fftfreq(len(signal), 1/sampleFreq))
    
    print("Plotting...")
    # Plot signal
    plt.figure("Signal and its FFT")
    plt.subplot(gs[0, :])
    plt.plot(time, signal, '.-')
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.title("Signal")
    plt.grid(True)
    
    # Plot FFT
    plt.subplot(gs[1, 0])
    plt.stem(freqAxis[freqAxis <= f_max], magSignal[freqAxis <= f_max])
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.title("FFT")
    plt.xlim(-1, 1)
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
    plt.show()


def TriangleWindow(sig):
    # Generate window
    window = np.zeros(N)
    window[0:int(N/2)] = np.arange(0, 1, 1/int(N/2))
    window[int(N/2):N] = np.arange(1, 0, -1/int(N/2))
    
    # Apply window
    sig = sig * window
    
    print("Window applied")
    
    return sig

sig = signalClass.Signal().y
# sig = constructSignal("sine", 5, PI/8)

SigFFT(sig)

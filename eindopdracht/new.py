import os, sys, traceback, scipy.io
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from scipy.signal import spectrogram

"""
Variables

Functions:
    - Getting a signal (class maybe)
    - Function for filters
    - Function for windows
    - Function for generating FFT data
    - Function for plotting

Main and errorhandling.
"""

sampleRate = 5000   # Hz
N = 20000           # Samples
cutoff = 100        # Hz
dBcutoff = 55       # dB
path = "signaal.mat"

def getSignal(path: str):
    """
    
    """
   
    dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), path)
    sig = np.reshape(scipy.io.loadmat(dir)['sig'], N)
    
    time = np.arange(len(sig)) / sampleRate
    
    return time, sig
    

def filterSignal(sig: np.ndarray, filter: str, poles: int = 5):
    """
    
    """
    global sampleRate, cutoff
    
    sos = scipy.signal.butter(poles, cutoff, filter, fs=sampleRate, output='sos')
    filteredSig = scipy.signal.sosfiltfilt(sos, sig)
    
    return filteredSig
    
def fftSignal(sig: np.ndarray, window: str = None):
    """
    
    """
    global sampleRate
    
    fftSig = np.fft.fftshift(np.fft.fft(sig) / len(sig))
    magSig = np.abs(fftSig) * 1 / np.sum(window) if window is not None else np.abs(fftSig)
    dBmagSig = 20 * np.log10(magSig / np.max(magSig))
    phiSignal = np.angle(fftSig)
    
    sFreq, sTime, sSpec = spectrogram(sig, sampleRate, nperseg=sampleRate, noverlap=sampleRate - 1, window=window if window is not None else 'boxcar', mode='magnitude')
    freqAxis = np.fft.fftshift(np.fft.fftfreq(len(sig), 1 / sampleRate))
    
    return magSig, dBmagSig, phiSignal, sFreq, sTime, sSpec, freqAxis
    

def multiPlot(x: np.ndarray, y: np.ndarray, title: str, xlabel: str, ylabel: str, loc: int = None, xlim: tuple = None, ylim: tuple = None, grid: bool = True, legend: bool = False):
    """
    
    """
    
    plt.subplot(loc) if loc is not None else plt.figure(title, figsize=(12, 8))    
    plt.plot(x, y)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.grid(grid)
    plt.legend() if legend else None
     
     
def main():
    """
    
    """
    
    time, sig = getSignal(path)
    magSig, dBmagSig, phiSignal, sFreq, sTime, sSpec, freqAxis = fftSignal(sig)
        
    multiPlot(time, sig, "Signal", "Time (s)", "Amplitude")
    
    plt.tight_layout()
    plt.show()
    
    return 0
    
    
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("An error occured: " + str(e))
        traceback.print_exc(file=sys.stdout, limit=2)
        sys.exit(1)
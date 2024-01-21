from cProfile import label
import os, sys, traceback, scipy.io
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import spectrogram

"""
Dit script voert signaalverwerkingsbewerkingen uit op een gegeven signaal.
Auteur: Job Siemerink
Datum: 22 December 2023
"""

sampleRate = 5000   # Hz
N = 20000           # Samples
fig = None          # Figure object
path = "signaal.mat"# Path naar het signaalbestand


def GetSignal(path: str):
    """
    Laad het signaal van het opgegeven pad.
    
    Args:
        path (str): Het pad naar het signaalbestand.
    
    Returns:
        tuple: Een tuple met het tijdsarray en het signaalarray.
    """
   
    dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), path)
    sig = np.reshape(scipy.io.loadmat(dir)['sig'], N)
    
    time = np.arange(len(sig)) / sampleRate
    
    return time, sig


def FilterSignal(sig: np.ndarray, filter: str, poles: int = 5):
    """
    Pas een digitaal filter toe op het invoersignaal.
    
    Args:
        sig (np.ndarray): Het invoersignaal.
        filter (str): Het type filter dat moet worden toegepast.
        poles (int, optioneel): Het aantal polen voor het filter. Standaard is 5.
    
    Returns:
        np.ndarray: Het gefilterde signaal.
    """
    global sampleRate, cutoff
    
    sos = scipy.signal.butter(poles, cutoff, filter, fs=sampleRate, output='sos')
    filteredSig = scipy.signal.sosfiltfilt(sos, sig)
    
    return filteredSig


def WindowSignal(sig: np.ndarray, window: str):
    """
    Pas een venster toe op het invoersignaal.
    
    Args:
        sig (np.ndarray): Het invoersignaal.
        window (str): Het type venster dat moet worden toegepast.
    
    Returns:
        np.ndarray: Het gevensterde signaal.
    """
    if window == "bartlett":
        return np.bartlett(len(sig)) * sig
    elif window == "hamming":
        return np.hamming(len(sig)) * sig
    else:
        return sig


def FFTSignal(sig: np.ndarray, padding: int = 0, window: str = None):
    """
    Voer FFT uit op het invoersignaal.
    
    Args:
        sig (np.ndarray): Het invoersignaal.
        window (str, optioneel): Het type venster dat moet worden toegepast. Standaard is None.
    
    Returns:
        tuple: Een tuple met het magnitude spectrum, dB magnitude spectrum, fase spectrum,
               spectrogram frequentie-as, spectrogram tijd-as, spectrogram en frequentie-as.
    """
    global sampleRate
    
    fftSig = np.fft.fftshift(np.fft.fft(sig, N + padding) / N)
    magSig = np.abs(fftSig) * 1 / np.sum(window) if window is not None else np.abs(fftSig)
    dBmagSig = 20 * np.log10(magSig / np.max(magSig))
    phiSignal = np.angle(fftSig)
    
    sFreq, sTime, sSpec= spectrogram(sig, fs=sampleRate)
    freqAxis = np.fft.fftshift(np.fft.fftfreq(len(fftSig), 1 / sampleRate))
    
    return magSig, dBmagSig, phiSignal, sFreq, sTime, sSpec, freqAxis


def MultiPlot(x: np.ndarray, y: np.ndarray, title: str, xlabel: str, ylabel: str, dBcutoff: int = 0, z: np.ndarray = None, plottype: str = 'plot', loc: int = 111, xlim: tuple = None, ylim: tuple = None, grid: bool = True, legend: bool = False, legend_label: str = None):
    """
    Plot meerdere signalen op dezelfde figuur.
    
    Args:
        x (np.ndarray): De waarden voor de x-as.
        y (np.ndarray): De waarden voor de y-as.
        title (str): De titel van de plot.
        xlabel (str): Het label voor de x-as.
        ylabel (str): Het label voor de y-as.
        z (np.ndarray, optioneel): De waarden voor de z-as voor 3D-plots. Standaard is None.
        plottype (str, optioneel): Het type plot dat gemaakt moet worden. Standaard is 'plot'.
        loc (int, optioneel): De locatie van de subplot. Standaard is 111.
        xlim (tuple, optioneel): De limieten voor de x-as. Standaard is None.
        ylim (tuple, optioneel): De limieten voor de y-as. Standaard is None.
        grid (bool, optioneel): Of er gridlijnen moeten worden weergegeven. Standaard is True.
        legend (bool, optioneel): Of de legenda moet worden weergegeven. Standaard is False.
    """
    global fig
    
    if fig is None:
        fig = plt.figure(title, figsize=(6*int(str(loc)[1]), 4*int(str(loc)[0])))
        
    plt.subplot(loc)
    
    
    if plottype == 'plot':
        if dBcutoff > 0:
            plt.plot(x, np.where(y > -dBcutoff, y, -dBcutoff), '-', label=legend_label)
            plt.plot(x, np.ones(len(x)) * -dBcutoff, 'k-')
        else:
            plt.plot(x, y, '-', label=legend_label)
    elif plottype == 'stem':
        plt.stem(x, y, label=legend_label)
    elif plottype == 'pcolormesh':
        plt.pcolormesh(x, y, 10 * np.log(z), shading='auto')
        plt.colorbar(label= "Intensity (dB)")
    elif plottype == 'scatter':
        plt.scatter(x, y, linewidths=0.1, s=1, label=legend_label)
        
    plt.title(title, fontdict={'fontsize': 14, 'fontweight': 'bold'})
    plt.xlabel(xlabel, fontdict={'fontsize': 14})
    plt.ylabel(ylabel, fontdict={'fontsize': 14})
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.grid(grid)
    plt.legend() if legend else None
    
    plt.tight_layout()

 
def main():
    """
    De hoofdfunctie van het script.
    """
    global fig, path
    
    cutoff = 750        # Hz
    dBcutoff = 53       # dB
    window = 'hamming'  # None, 'bartlett', 'hamming'
    
    # Maken van verschillende plots
    tijd, sig = GetSignal(path)    
    
    
    # Plot die het signaal weergeeft samen met alle mogelijke plots uit dit script
    fig = None
    magSig, dBmagSig, phiSignal, sFreq, sTime, sSpec, freqAxis = FFTSignal(sig, padding=1000000)
    MultiPlot(tijd, sig, "Signaal", "Tijd (s)", "Amplitude", plottype='plot', loc=221)
    MultiPlot(freqAxis, dBmagSig, "Amplitude spectrum", "Frequentie (Hz)", "Magnitude (dB)", dBcutoff=dBcutoff, plottype='plot', loc=222)
    MultiPlot(sTime, sFreq, "Spectrogram", "Frequentie (Hz)", "Tijd (s)", z=sSpec, plottype='pcolormesh', loc=223, grid=False)
    MultiPlot(freqAxis, phiSignal, "Fase spectrum", "Frequentie (Hz)", "Fase (rad)", plottype='scatter', loc=224, grid=False)
    
    
    
    # Plot die het amplitude spectrum van het signaal weergeeft en vergelijkt tussen padding en geen padding.
    fig = None
    magSig, dBmagSig, phiSignal, sFreq, sTime, sSpec, freqAxis = FFTSignal(sig, padding=1000000)
    MultiPlot(freqAxis, dBmagSig, "Amplitude spectrum", "Frequentie (Hz)", "Magnitude (dB)", dBcutoff=dBcutoff, plottype='plot', loc=121, legend=True, legend_label="Met padding")
    MultiPlot(freqAxis, dBmagSig, "Ingezoomed spectrum", "Frequentie (Hz)", "Magnitude (dB)", plottype='plot', loc=122, xlim=(498, 502), ylim=(-50, 0), legend=True, legend_label="Met padding")
    magSig, dBmagSig, phiSignal, sFreq, sTime, sSpec, freqAxis = FFTSignal(sig)    
    MultiPlot(freqAxis, dBmagSig, "Amplitude spectrum", "Frequentie (Hz)", "Magnitude (dB)", dBcutoff=dBcutoff, plottype='plot', loc=121, legend=True, legend_label="Zonder padding")
    MultiPlot(freqAxis, dBmagSig, "Ingezoomed spectrum", "Frequentie (Hz)", "Magnitude (dB)", plottype='plot', loc=122, xlim=(498, 502), ylim=(-50, 0), legend=True, legend_label="Zonder padding")
    
    
    fig = None
     
    
    
    
    plt.show()
    
    return 0


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("An error occured: " + str(e))
        traceback.print_exc(file=sys.stdout)
        sys.exit(1)
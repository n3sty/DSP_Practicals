import os, sys, traceback, scipy.io
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import spectrogram

"""
This script performs signal processing operations on a given signal.
#TODO: make the windows work
#TODO: make the filters work
"""

sampleRate = 5000   # Hz
N = 20000           # Samples
fig = None
path = "signaal.mat"


def GetSignal(path: str):
    """
    Load the signal from the specified path.
    
    Args:
        path (str): The path to the signal file.
    
    Returns:
        tuple: A tuple containing the time array and the signal array.
    """
   
    dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), path)
    sig = np.reshape(scipy.io.loadmat(dir)['sig'], N)
    
    time = np.arange(len(sig)) / sampleRate
    
    return time, sig


def FilterSignal(sig: np.ndarray, filter: str, poles: int = 5):
    """
    Apply a digital filter to the input signal.
    
    Args:
        sig (np.ndarray): The input signal.
        filter (str): The type of filter to apply.
        poles (int, optional): The number of poles for the filter. Defaults to 5.
    
    Returns:
        np.ndarray: The filtered signal.
    """
    global sampleRate, cutoff
    
    sos = scipy.signal.butter(poles, cutoff, filter, fs=sampleRate, output='sos')
    filteredSig = scipy.signal.sosfiltfilt(sos, sig)
    
    return filteredSig


def WindowSignal(sig: np.ndarray, window: str):
    """
    Apply a window to the input signal.
    
    Args:
        sig (np.ndarray): The input signal.
        window (str): The type of window to apply.
    
    Returns:
        np.ndarray: The windowed signal.
    """
    if window == "bartlett":
        return np.bartlett(len(sig)) * sig
    elif window == "hamming":
        return np.hamming(len(sig)) * sig
    else:
        return sig


def FFTSignal(sig: np.ndarray, padding: int = 0, window: str = None):
    """
    Perform FFT on the input signal.
    
    Args:
        sig (np.ndarray): The input signal.
        window (str, optional): The type of window to apply. Defaults to None.
    
    Returns:
        tuple: A tuple containing the magnitude spectrum, dB magnitude spectrum, phase spectrum,
               spectrogram frequency axis, spectrogram time axis, spectrogram, and frequency axis.
    """
    global sampleRate
    
    fftSig = np.fft.fftshift(np.fft.fft(sig, N + padding) / N)
    magSig = np.abs(fftSig) * 1 / np.sum(window) if window is not None else np.abs(fftSig)
    dBmagSig = 20 * np.log10(magSig / np.max(magSig))
    phiSignal = np.angle(fftSig)
    
    sFreq, sTime, sSpec = spectrogram(sig, sampleRate)
    freqAxis = np.fft.fftshift(np.fft.fftfreq(len(fftSig), 1 / sampleRate))
    
    return magSig, dBmagSig, phiSignal, sFreq, sTime, sSpec, freqAxis


def MultiPlot(x: np.ndarray, y: np.ndarray, title: str, xlabel: str, ylabel: str, dBcutoff: int = 0, z: np.ndarray = None, plottype: str = 'plot', loc: int = 111, xlim: tuple = None, ylim: tuple = None, grid: bool = True, legend: bool = False):
    """
    Plot multiple signals on the same figure.
    
    Args:
        x (np.ndarray): The x-axis values.
        y (np.ndarray): The y-axis values.
        title (str): The title of the plot.
        xlabel (str): The label for the x-axis.
        ylabel (str): The label for the y-axis.
        z (np.ndarray, optional): The z-axis values for 3D plots. Defaults to None.
        plottype (str, optional): The type of plot to create. Defaults to 'plot'.
        loc (int, optional): The location of the subplot. Defaults to 111.
        xlim (tuple, optional): The limits for the x-axis. Defaults to None.
        ylim (tuple, optional): The limits for the y-axis. Defaults to None.
        grid (bool, optional): Whether to show grid lines. Defaults to True.
        legend (bool, optional): Whether to show the legend. Defaults to False.
    """
    global fig
    
    if fig is None:
        fig = plt.figure(title, figsize=(6*int(str(loc)[1]), 4*int(str(loc)[0])))
        
    plt.subplot(loc)
    
    
    if plottype == 'plot':
        if dBcutoff > 0 and title == "FFT":
            plt.plot(x, np.where(y > -dBcutoff, y, -dBcutoff), '-')
            plt.plot(x, np.ones(len(x)) * -dBcutoff, 'r-')
        else:
            plt.plot(x, y, '-')
    elif plottype == 'stem':
        plt.stem(x, y)
    elif plottype == 'pcolormesh':
        plt.pcolormesh(x, y, 10 * np.log(z))
        plt.colorbar(label= "Intensity (dB)")
    elif plottype == 'scatter':
        plt.scatter(x, y, linewidths=0.1, s=1)
        
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
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
    dBcutoff = 0       # dB
    window = 'hamming'  # None, 'bartlett', 'hamming'
    
    # # RAUW SIGNAAL, GEEN BEWERKINGEN
    # tijd, sig = GetSignal(path)
    # magSig, dBmagSig, phiSignal, sFreq, sTime, sSpec, freqAxis = FFTSignal(sig)
        
    # MultiPlot(tijd, sig, "Signaal", "Tijd (s)", "Amplitude", plottype='plot', loc=121)
    # MultiPlot(freqAxis, dBmagSig, "FFT", "Frequentie (Hz)", "Magnitude (dB)", dBcutoff=dBcutoff, plottype='plot', loc=122)
    # MultiPlot(sTime, sFreq, "Spectrogram", "Tijd (s)", "Frequentie (Hz)", z=sSpec, plottype='pcolormesh', loc=223, grid=False)
    # MultiPlot(freqAxis, phiSignal, "Fasediagram", "Frequentie (Hz)", "Fase (rad)", plottype='scatter', loc=224)
    
    # fig = None
    
    # # GEFILTERD SIGNAAL
    # tijd, sig = GetSignal(path)
    # sig = FilterSignal(sig, "lowpass", poles=3)
    # magSig, dBmagSig, phiSignal, sFreq, sTime, sSpec, freqAxis = FFTSignal(sig)
    
    # MultiPlot(tijd, sig, "Gefilterd signaal", "Tijd (s)", "Amplitude", plottype='plot', loc=121)
    # MultiPlot(freqAxis, dBmagSig, "FFT", "Frequentie (Hz)", "Magnitude (dB)", plottype='plot', loc=122)
    # # MultiPlot(sTime, sFreq, "Spectrogram", "Tijd (s)", "Frequentie (Hz)", z=sSpec, plottype='pcolormesh', loc=223, grid=False)
    # # MultiPlot(freqAxis, phiSignal, "Fasediagram", "Frequentie (Hz)", "Fase (rad)", plottype='scatter', loc=224)
    
    fig = None
    
    # GEWINDOWED SIGNAAL 
    tijd, sig = GetSignal(path)
    # sig = WindowSignal(sig, window)
    magSig, dBmagSig, phiSignal, sFreq, sTime, sSpec, freqAxis = FFTSignal(sig)
    
    MultiPlot(tijd, sig, "Gewindowed signaal", "Tijd (s)", "Amplitude", plottype='plot', loc=121)
    MultiPlot(freqAxis, dBmagSig, "FFT", "Frequentie (Hz)", "Magnitude (dB)", dBcutoff=dBcutoff, plottype='plot', loc=122)
    # MultiPlot(sTime, sFreq, "Spectrogram", "Tijd (s)", "Frequentie (Hz)", z=sSpec, plottype='pcolormesh', loc=223, grid=False)
    # MultiPlot(freqAxis, phiSignal, "Fasediagram", "Frequentie (Hz)", "Fase (rad)", plottype='scatter', loc=224)
    
    fig = None
    
    # GEPAD SIGNAAL 
    tijd, sig = GetSignal(path)
    # sig = WindowSignal(sig, window)
    magSig, dBmagSig, phiSignal, sFreq, sTime, sSpec, freqAxis = FFTSignal(sig, padding=100000)
    
    MultiPlot(tijd, sig, "Gepad & gewindowed signaal", "Tijd (s)", "Amplitude", plottype='plot', loc=121)
    MultiPlot(freqAxis, dBmagSig, "FFT", "Frequentie (Hz)", "Magnitude (dB)", dBcutoff=dBcutoff, plottype='plot', loc=122)
    
    # # GEWINDOWED, GEFILTERD SIGNAAL, IN DIE VOLGORDE
    # sig = FilterSignal(sig, "lowpass", poles=3)
    # magSig, dBmagSig, phiSignal, sFreq, sTime, sSpec, freqAxis = FFTSignal(sig)
    
    # MultiPlot(tijd, sig, "Gefilterd & gewindowed signaal", "Tijd (s)", "Amplitude", plottype='plot', loc=121)
    # MultiPlot(freqAxis, dBmagSig, "FFT", "Frequentie (Hz)", "Magnitude (dB)", plottype='plot', loc=122)
    # # MultiPlot(sTime, sFreq, "Spectrogram", "Tijd (s)", "Frequentie (Hz)", z=sSpec, plottype='pcolormesh', loc=223, grid=False)
    # # MultiPlot(freqAxis, phiSignal, "Fasediagram", "Frequentie (Hz)", "Fase (rad)", plottype='scatter', loc=224)

    plt.show()
    
    return 0


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("An error occured: " + str(e))
        traceback.print_exc(file=sys.stdout)
        sys.exit(1)
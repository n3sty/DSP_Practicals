from asyncio.constants import FLOW_CONTROL_HIGH_WATER_SSL_READ
import os, sys, traceback, scipy.io
from matplotlib import figure
from random import sample
from tkinter import font
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from scipy.signal import spectrogram

# Declaring variables
PI = np.pi
seperateFigures = False     # Option to plot the signal and FFT in seperate figures
sampleRate = 5000           # Hz
filterFreq = 100            # Hz
N = 4 * sampleRate          # 1/2 periods times sample frequency = number of samples
freq = 2                   # Hz
cutoff = 54.5               # dB, set 0 to disable, set positive to limit the dB range
gs = gridspec.GridSpec(2, 2)

def loadSignal(filename: str = None, window = None, filter = None, padding: int = 0) -> np.ndarray:
    # Loading the signal from the .mat file and reshaping it to a 1-dimensional array
    sig = np.reshape(scipy.io.loadmat(os.path.join(os.path.dirname(os.path.realpath(__file__)), filename))['sig'], N)
    
    if window == "bartlett":
        sig = np.bartlett(len(sig)) * sig
    elif window == "hamming":
        sig = np.hamming(len(sig)) * sig
    
    # !!! Kijk of je niet het frequentiedomein moet filteren ipv het tijdsdomein !!! #
    if filter is not None:
        signal = Filter.filter(type=filter, data=signal, cutoff=filterFreq, sampleFreq=sampleRate)
    
    sig = np.append(sig, np.zeros(padding)) if padding > 0 else sig
    time = np.arange(len(sig)) / sampleRate
    
    return time, sig


class Filters:
    def __init__(self) -> None:
        pass
    def filter(self, type: str, data: np.ndarray, cutoff: float, sampleFreq: float, poles: int = 5) -> np.ndarray:
        
        if type == "lowpass":
            return self.lowpass(data, cutoff, sampleFreq, poles)
        elif type == "highpass":
            return self.highpass(data, cutoff, sampleFreq, poles)
        
    def lowpass(self, data: np.ndarray, cutoff: float, sampleFreq: float, poles: int = 5) -> np.ndarray:
        """
        Apply a lowpass filter to the input data.

        Args:
            data (np.ndarray): The input data to be filtered.
            cutoff (float): The cutoff frequency of the filter.
            sampleFreq (float): The sampling frequency of the input data.
            poles (int, optional): The number of poles in the filter. Defaults to 5.

        Returns:
            np.ndarray: The filtered data.
        """
        sos = scipy.signal.butter(poles, cutoff, 'lowpass', fs=sampleFreq, output='sos')
        filteredData = scipy.signal.sosfiltfilt(sos, data)
        return filteredData
    
    def highpass(self, data: np.ndarray, cutoff: float, sampleFreq: float, poles: int = 5) -> np.ndarray:
        """
        Apply a highpass filter to the input data.

        Args:
            data (np.ndarray): The input data to be filtered.
            cutoff (float): The cutoff frequency of the filter.
            sampleFreq (float): The sampling frequency of the input data.
            poles (int, optional): The number of poles in the filter. Defaults to 5.

        Returns:
            np.ndarray: The filtered data.
        """
        sos = scipy.signal.butter(poles, cutoff, 'highpass', fs=sampleFreq, output='sos')
        filteredData = scipy.signal.sosfiltfilt(sos, data)
        return filteredData


def constructSignal(signal_type, order, sampleRate, padding=0, phase=0):
    """
    Construct a signal of a given type, order, and phase.

    Parameters:
    signal_type (str): The type of signal to generate. Currently supports "sine".
    order (int): The order of the signal, which determines the number of harmonics.
    phase (float, optional): The phase offset of the signal in radians. Defaults to 0.

    Returns:
    numpy.ndarray: The generated signal as a 1-dimensional numpy array.
    """
    # Checking the input data for validity
    if signal_type != "sine":
        raise ValueError("Invalid signal type. Only 'sine' is supported.")

    time = np.arange(N) / sampleRate
    sig = np.zeros(N)

    for i in range(1, order + 1):
        sine = 1 / i * np.sin(freq * i * 2 * PI * time + phase)
        sign = -1 if i % 2 == 0 else 1
        sig = sig + sine * sign

    # sig = sig * np.sin(2 * PI * time)
    
    if padding:
        sig = np.append(sig, np.zeros(padding))
        time = np.append(time, (np.arange(padding) / sampleRate))
    
    return time, sig


def SigFFT(time, signal, title, padding=0, window=None, cutoff=0, fig=None):
    """
    Calculate and plot the Fast Fourier Transform (FFT) of a given signal.

    Parameters:
    - time (array-like): Time values corresponding to the signal data.
    - signal (array-like): Input signal data.
    - title (str): Title for the plot.
    - window (array-like, optional): Window function to apply to the signal. Default is None.
    - cutoff (float, optional): Cutoff value for plotting the FFT in dB. Default is 0.
    - fig (int, optional): Figure number for the plot. Default is None.

    Returns:
    None
    """
    # Checking the input data for validity

    gs = gridspec.GridSpec(1, 2)

    signal = signal * window if window is not None else signal

    # Calculating the FFT    
    fftSignal = np.fft.fftshift(np.fft.fft(signal, len(signal) + padding) / len(signal))
    magSignal = np.abs(fftSignal) * N / np.sum(window) if window is not None else np.abs(fftSignal)
    dBmagSignal = 20 * np.log10(magSignal / np.max(magSignal))
    phiSignal = np.angle(fftSignal)
    
    frequencies, times, spectrogramData = spectrogram(signal, sampleRate)
    freqAxis = np.fft.fftshift(np.fft.fftfreq(len(fftSignal), 1 / sampleRate))
    
    
    if seperateFigures:
        # Plotting the signal
        plt.figure(fig)
        plt.plot(time, signal, '-', linewidth=0.5)
        if window is not None:
            plt.plot(time, window, '--', linewidth=2)
        plt.xlabel("Tijd (s)")
        plt.ylabel("Amplitude")
        plt.title("Signaal")
        plt.legend(["Signaal", "Window"])
        plt.grid(True)
        
        # Plotting the FFT
        plt.figure(fig)
        
        # Plot the signal in dB, but only up to the cutoff if the cutoff is defined
        if cutoff > 0:
            plt.plot(freqAxis, np.where(dBmagSignal > -cutoff, dBmagSignal, -cutoff), '-', linewidth=0.5)
            plt.plot(freqAxis, np.ones(len(freqAxis)) * -cutoff, 'r-', linewidth=0.5)
        else:
            plt.plot(freqAxis, magSignal, '-', linewidth=0.5)
        
        plt.xlabel("Frequentie (Hz)")
        plt.ylabel("Intensiteit (dB)")
        plt.title("Amplitude spectrum")
        plt.grid(True)
    else:
        
        if fig is None:
            fig = plt.figure(title, figsize=(10, 3))
        else:
            plt.figure(fig)
        
        # Plotting the signal
        plt.subplot(gs[0, 0])
        plt.plot(time, signal, '-')
        if window is not None:
            plt.plot(time, window, '--', linewidth=2)
        plt.xlabel("Tijd (s)")
        plt.ylabel("Amplitude")
        plt.title("Signaal", fontweight='bold')
        # plt.xlim(0, 1)
        # plt.legend(["Signaal", "Window"])
        plt.grid(False)
        

        # Plotting the FFT
        plt.subplot(gs[0, 1])

        # Plot the signal in dB, but only up to the cutoff if the cutoff is defined
        if cutoff > 0:
            plt.plot(freqAxis, np.where(dBmagSignal > -cutoff, dBmagSignal, -cutoff), '-')
            plt.plot(freqAxis, np.ones(len(freqAxis)) * -cutoff, 'r-')
        else:
            plt.plot(freqAxis, magSignal, '-')
        
        plt.xlabel("Frequentie (Hz)")
        plt.ylabel("Amplitude")
        plt.xlim(-20, 20)
        plt.title("Amplitude spectrum", fontweight='bold')
        plt.grid(False)
        

    plt.tight_layout()


if __name__ == "__main__":
    print("Starting...")
    try:
        seperateFigures = False
        Filter = Filters()
        cutoff = 0
        sampleRate = 5000
        """
        Compute the FFT and plot the signal, windows are useable with the following commands:
                'bartlett' for triangle, 'hamming' for hamming, etc.
        
        Usage of filters is done by addin a filter argument to the SigFFT function:
                'lowpass' for lowpass filter, 'highpass' for highpass filter
        """

        fig = plt.figure("Simpel signaal", figsize=(10, 4))
        time, signal = constructSignal("sine", 2, sampleRate, 0)
        SigFFT(time, signal, "Simpel signaal", fig=fig)
        
        fig = plt.figure("Simpel signaal met zero-padding", figsize=(10, 4))
        time, signal = constructSignal("sine", 2, sampleRate, 100000, 0)
        SigFFT(time, signal, "Simpel signaal", padding=100000, fig=fig)
        
        fig = plt.figure("Simpel signaal met ruis en een low-pass filter", figsize=(10, 4))
        time, signal = constructSignal("sine", 2, sampleRate, 0)
        signal = signal + np.random.normal(0, 1, len(signal))
        signal = Filter.filter(type="lowpass", data=signal, cutoff=20, sampleFreq=sampleRate)
        SigFFT(time, signal, "Simpel signaal", fig=fig)

        
        fig = plt.figure("Simpel signaal met driekhoek-window", figsize=(10, 4))
        time, signal = constructSignal("sine", 2, sampleRate, 0)
        SigFFT(time, signal, "Simpel signaal", window=np.bartlett(N), cutoff=cutoff, fig=fig)
        plt.show()

    except FileNotFoundError:
        print("Error: 'signaal.mat' file not found.")
    except Exception as e:
        traceback.print_exc(2)
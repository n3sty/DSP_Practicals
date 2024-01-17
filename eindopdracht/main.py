import numpy as np
import os
import scipy.io
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from scipy.signal import spectrogram

# Declaring variables
PI = np.pi
sampleFreq = 5000  # Hz
N = 4 * sampleFreq  # 1/2 periods times sample frequency = number of samples
freq = 20  # Hz
cutoff = 55  # dB
gs = gridspec.GridSpec(2, 2)


def constructSignal(signal_type, order, phase=0):
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

    print("Generating signal...")
    time = np.arange(N) / sampleFreq
    sig = np.zeros(N)

    for i in range(1, order + 1):
        sine = 1 / i * np.sin(freq * i * 2 * PI * time + phase)
        sign = -1 if i % 2 == 0 else 1
        sig = sig + sine * sign

    sig = sig * np.sin(2 * PI * time)
    print("Signal generated")
    return sig


def SigFFT(yData, title, window=None, cutoff=0):
    """
    Calculate and plot the Fast Fourier Transform (FFT) of a given signal.

    Parameters:
    - yData (array-like): Input signal data.
    - title (str): Title for the plot.
    - window (array-like, optional): Window function to apply to the signal. Default is None.

    Returns:
    None
    """
    # Checking the input data for validity
    if window is not None and not isinstance(window, np.ndarray):
        raise ValueError("Invalid window type. Please provide a numpy array or None.")

    # Calculating the FFT
    print("Calculating FFT...")
    time = np.arange(N) / sampleFreq
    signal = yData * window if window is not None else yData
    
    fftSignal = np.fft.fftshift(np.fft.fft(signal) / len(signal))
    magSignal = np.abs(fftSignal) * 1 / np.sum(window) if window is not None else np.abs(fftSignal) * 2
    dBmagSignal = 20 * np.log10(magSignal / np.max(magSignal))
    phiSignal = np.angle(fftSignal)
    
    frequencies, times, spectrogramData = spectrogram(yData, sampleFreq)
    freqAxis = np.fft.fftshift(np.fft.fftfreq(len(signal), 1 / sampleFreq))
    print("FFT calculated")


    # Generating the window
    plt.figure(title, figsize=(12, 8))
    print("Plotting...")
    
    # Plotting the signal
    plt.subplot(gs[0, 0])
    plt.plot(time, signal, '-', linewidth=0.5)
    if window is not None:
        plt.plot(time, window, '--', linewidth=0.5)
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.title("Signal")
    plt.grid(True)
    
    # Plotting the spectrogram
    plt.subplot(gs[0, 1])
    plt.pcolormesh(times, frequencies, 10 * np.log(spectrogramData))
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [sec]')
    plt.title("Spectrogram")
    plt.colorbar(label= "Intensity (dB)")

    # Plotting the FFT
    plt.subplot(gs[1, 0])

    # Plot the signal in dB, but only up to the cutoff if the cutoff is defined
    if cutoff > 0:
        plt.plot(freqAxis / 1000, np.where(dBmagSignal > -cutoff, dBmagSignal, -cutoff), '-', linewidth=2)
        plt.plot(freqAxis / 1000, np.ones(len(freqAxis)) * -cutoff, 'r-', linewidth=0.5)
    else:
        plt.plot(freqAxis / 1000, dBmagSignal, '-', linewidth=2)
    
    plt.xlabel("Frequency (kHz)")
    plt.ylabel("Magnitude (dB)")
    plt.title("FFT")
    plt.grid(True)

    # Plotting the phase
    plt.subplot(gs[1, 1])
    plt.plot(freqAxis, phiSignal/np.pi, '-', linewidth=0.5)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Phase (pi * rad)")
    plt.title("Phase")
    plt.grid(True)

    plt.tight_layout()

    print("Plots generated")


if __name__ == "__main__":
    print("Starting...")
    try:
        sig = np.reshape(scipy.io.loadmat(os.path.join(os.path.dirname(os.path.realpath(__file__)), "signaal.mat"))['sig'], 20000)
    
        # np.bartlett for triangle, np.hamming for hamming, etc.
        SigFFT(sig, "Rectangular", None, cutoff)
        SigFFT(sig, "Bartlett", np.bartlett(N), cutoff)  
        SigFFT(sig, "Hanning", np.hanning(N), cutoff)
        
        print("Done")
        plt.show()

    except FileNotFoundError:
        print("Error: 'signaal.mat' file not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

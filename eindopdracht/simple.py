import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# Declaring variables
sampleFreq = 10 # Hz
N = 100 # Samples
freq = 1/10 # Hz
gs = gridspec.GridSpec(2, 2)

# Generate signal
time = np.arange(N) / sampleFreq
signal = np.sin(freq * 2*np.pi*time) + np.sin(freq*4 * 2*np.pi*time)**2 - 1/2 * np.sin(freq * 2*np.pi*time)**3
fftSignal = np.fft.fftshift(np.fft.fft(signal) / len(signal))
magSignal = np.abs(fftSignal)
phiSignal = np.angle(fftSignal)

# Generate frequency axis
freqAxis = np.fft.fftshift(np.fft.fftfreq(len(signal), 1/sampleFreq))

# Plot signal
plt.figure("Signal")
plt.subplot(gs[0, :])
plt.plot(time, signal, '.-')
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
# plt.xlim(-1, 1)
plt.grid(True)

# Plot phase
plt.subplot(gs[1, 1])
plt.stem(freqAxis, phiSignal)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Phase (rad)")
plt.title("Phase")
plt.grid(True)

plt.tight_layout()  # Add this line to adjust the spacing between subplots
plt.show()



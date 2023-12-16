from scipy import signal
import numpy as np
from matplotlib import animation
import matplotlib.pyplot as plt


PI = np.pi

class DiscreteFunctions():
    
    def DiscFuncA(n):
        return 5 + np.sin(n*PI/2) + np.cos(n*PI/4)
    


def DiscFuncB(n):
    return np.cos((n*PI)/2 - (PI/4))


def animate(i):
    line.set_ydata(np.abs(np.fft.fftshift(np.fft.fft(DiscreteFunctions.DiscFuncA(np.arange(0, i*PI, .1))))))
    return line,


def main():
    global line, fig, n
    
    
    n = np.arange(0, 5*PI, .1)
    
    fft = np.fft.fft(DiscFuncB(n))
    fft = np.fft.fftshift(np.fft.fft(DiscreteFunctions.DiscFuncA(n)))
    
    n = np.fft.fftshift(np.fft.fftfreq(len(n)))
    
    
    plt.figure()
    plt.title("Fourier Transform (abs)")
    plt.ylabel("Magnitude")
    plt.plot(n/PI, np.abs(fft))
    plt.xlabel("Frequency/PI")    
    plt.show()
    
    return 0



if __name__ == "__main__":
    main()
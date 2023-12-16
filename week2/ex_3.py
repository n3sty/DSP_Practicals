<<<<<<< HEAD
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt



def FFTConvolve(IN1, IN2):
    
    y = signal.fftconvolve(IN1, IN2, 'same')
    
    return y


def DiracDelta(x, offset:int=0):
    
    val = np.zeros_like(x)
    val[x==offset] = 1
    
    return val


def plot(x:np.ndarray, y:np.ndarray):
    
    plt.figure()
    plt.plot(x, y)
    plt.title("Walking Mean")
    
    return 0


def main():
    
    M = 50
    length = 2*M
    xRange = np.arange(0, length)
    
    IN1 = DiracDelta(xRange, length/2)
    IN2 = np.ones(M)/M

    plot(xRange, FFTConvolve(IN1, IN2))
    
    plt.show()

        
    return 0


if __name__ == "__main__":
=======
from scipy import signal
import matplotlib.pyplot as plt
from matplotlib import gridspec
import numpy as np


def x(i):
    return i


def DiscreteFunc(vals, M):
    
    y = np.zeros(len(vals))
    s = 0
    
    for n in vals:
        y[n] = 1/(M+1) * sum(x(n-k).real for k in range(M))
        
    return y


def PlotWalkingMean(samples, y_in):
    
    gc = gridspec.GridSpec(1, 2)
    plt.figure()
    
    plt.subplot(gc[0,0])
    plt.title('Walking Mean')
    plt.plot(samples, y_in)
    plt.xlabel('Samples (n)')
    plt.ylabel('Amplitude')
    
    plt.subplot(gc[0, 1])
    plt.title('Input function')
    plt.plot(samples, x(samples).real)
    plt.xlabel('Samples (n)')
    plt.ylabel('Amplitude')
    
    plt.show()
    
    return 0


def main():
    
    samples = np.arange(100, dtype=int)
    
    PlotWalkingMean(samples, DiscreteFunc(samples, 5))
    
    


if __name__ == "__main__":
>>>>>>> 7a821c19ec9a54430d6097227786b5ac2a47c709
    main()
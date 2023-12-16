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
    main()
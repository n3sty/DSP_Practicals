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
    main()
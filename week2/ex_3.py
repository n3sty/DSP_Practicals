import numpy as np
import func
import matplotlib.pyplot as plt
from scipy import signal

def Impulse(n):
    return func.Delta(n)

def Step(n):
    return func.Step(n)

def Custom(n):
    x = []
    
    for i in n:
        x.append(np.sin(2*np.pi*i/60) + np.sin(2*np.pi*i/10))
    
    return x


def Convolution(input:callable, n:np.ndarray, M:int):
    
    walkingMean = np.ones(M)/M
    
    y = np.convolve(input(n), walkingMean, mode='same')
    
    return y


def opdracht_3a():
    
    yData = Convolution(Impulse, n, M)
    
    plt.figure()
    plt.stem(n, yData)
    
    return yData


def opdracht_3b():
    
    num = np.ones(M)/M
    den = [1]
    
    return num, den


def opdracht_3c():
    
    imp = Convolution(Impulse, n, M)
    plt.figure()
    plt.subplot(211)
    plt.stem(imp)
    
    step = Convolution(Step, n, M)
    plt.subplot(212)
    plt.stem(step)
    
    return
    

def opdracht_3d(num, den):
    
    freqs, H = signal.freqz(num, den)
    
    plt.figure()
    plt.stem(freqs, np.abs(H))
    
    return


def opdracht_3f(num, den):
    
    yData = signal.lfilter(num, den, Custom(n))
    
    plt.figure()
    plt.stem(yData)
    
    return yData


def main():
    global n, M
    
    n = func.Indices(40)
    M = 10
    
    opdracht_3a()
    num, den = opdracht_3b()
    opdracht_3c()
    opdracht_3d(num, den)
    opdracht_3f(num, den)
    
    
    plt.show()
    
    return 0


if __name__ == "__main__":
    main()
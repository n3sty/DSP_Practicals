from scipy import signal
import numpy as np
import matplotlib.pyplot as plt


def TransferFunction(IN, M, dt):
    
    num = np.zeros(M)
    den = np.zeros(M)
    
    for n in range(M):
        for k in range(M):
            num[n] = IN[n-k]
            den[n] = IN[n-k]
    

    
    return signal.TransferFunction(num, den, dt=dt)

def plot(x:np.ndarray, y:np.ndarray):
    
    plt.figure()
    plt.plot(x, y)
    
    return 0


def main():
    
    M = 10
    length = 2*M
    dt = 1
    xRange = np.arange(-length, length)
    
    tf = TransferFunction(xRange, M, dt)
        
    tout, yout = signal.dimpulse(tf)

    plot(tout, yout[0])
    
    plt.show()

        
    return 0


if __name__ == "__main__":
    main()
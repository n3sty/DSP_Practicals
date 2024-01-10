import numpy as np
import func
import matplotlib.pyplot as plt
from scipy import signal

# Easy-access functions used as inputs further on
def Impulse(n):
    return func.Delta(n)

def Step(n):
    return func.Step(n)

def Custom(n):
    x = []
    
    for i in n:
        x.append(np.sin(2*np.pi*i/60) + np.sin(2*np.pi*i/10))
    
    return x

# To compute the moving average (or 'walking mean') I have used convolution with the transferfunction form of the moving average
# discrete summation. This seems to work better than when I implement the entire algorithm myself manually :).
def Convolution(input:callable, n:np.ndarray, M:int):
    """
        This function takes other functions as its input, to generate a different dataset with each function. The result is a 
        moving average over the inputted function, which essentially acts as a low-pass filter.
        
        M is the window size of the moving average.
        
        :returns: y: np.ndarray with 'filtered' data.
    """
    walkingMean = np.ones(M)/M
    
    # Numpy convolution method, mode='same' gives back an array of the same size as the input was, making plotting easier.
    y = np.convolve(input(n), walkingMean, mode='same')
    
    return y

# Impulse response of the moving average.
def opdracht_3a():
    
    yData = Convolution(Impulse, n, M)
    
    plt.figure()
    plt.title("Impulse response")
    plt.stem(n, yData)
    plt.xlabel('n')
    plt.ylabel('x[n]')
    
    return yData

# Generate the numerator and denominator (or a's and b's) for the moving average
def opdracht_3b():
    
    num = np.ones(M)/M
    den = [1]
    
    return num, den

# Impulse and Step-response of the moving average filter.
def opdracht_3c():
    
    imp = Convolution(Impulse, n, M)
    plt.figure("Opdracht 3c")
    plt.subplot(211)
    plt.title("Impulse en Step-response")
    plt.stem(imp)
    plt.ylabel('x[n]')
    
    step = Convolution(Step, n, M)
    plt.subplot(212)
    plt.stem(step)
    plt.xlabel('n')
    plt.ylabel('x[n]')
    
    return
    
# Frequency response of the moving average filter.
def opdracht_3d(num, den):
    
    freqs, H = signal.freqz(num, den)
    
    plt.figure()
    plt.title("Frequency Response")
    plt.stem(freqs, np.abs(H))
    plt.xlabel("Frequencies (s^-1)")
    plt.ylabel("Magnitude |H|")
    
    return

# Response of the filter with a custom function (sinusoid) as input.
def opdracht_3f(num, den):
    
    # signal.lfilter is the python discrete equivalent of Matlab's 'filter'.
    yData = signal.lfilter(num, den, Custom(n))
    
    plt.figure()
    plt.title("Custom response")
    plt.plot(Custom(n), 'g', label='input')
    plt.stem(yData, label='output')
    plt.xlabel('n')
    plt.ylabel('x[n]')
    plt.legend()
    
    return yData


def main():
    # Because they are accessed in every excercise, they are made global for minimal repeated declarations.
    global n, M
    
    n = func.Indices(40)
    M = 10
    
    # Running all exercises
    opdracht_3a()
    num, den = opdracht_3b()
    opdracht_3c()
    opdracht_3d(num, den)
    opdracht_3f(num, den)
    
    plt.show()
    
    return


if __name__ == "__main__":
    main()
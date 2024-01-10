import numpy as np
import matplotlib.pyplot as plt

# Declaring constants
PI = np.pi


def fourier_series(inputFunc:callable):
    """
    The function `fourier_series` calculates the Fourier series coefficients for a given input function.
    
    :param inputFunc: The inputFunc parameter is a callable object that takes no arguments and returns a
    tuple containing two elements: x and N
    :type inputFunc: callable
    :return: The function `fourier_series` returns an array `a` which contains the coefficients of the
    Fourier series of the input function.
    """
    
    x, N = inputFunc()
    a = np.zeros(N, dtype=complex)
    
    # The nested for-loop that encapsulates the Discrete Fourier Series
    for k in range(N):
        sum = 0
        
        # n in range(N) excludes N, so in mathematical notations it would be "the sum from n=0 to N-1"
        for n in range(N):            
            sum += (x[n] * np.exp(-1j * k * 2*PI/N * n))
        a[k] = 1/N * sum

    return a


def inv_fourier_series(a):
    """
    The function `inv_fourier_series` calculates the inverse discrete Fourier transform of a given
    sequence of coefficients `a`.
    
    :param a: The parameter "a" is a list or array of coefficients representing the Fourier coefficients
    :return: two values: "samples" and "x". "samples" is an array containing the indices of the samples,
    and "x" is an array containing the values of the inverse Fourier series.
    """
    
    N = len(a)
    samples = np.arange(N)
    x = np.zeros(N, dtype=complex)
    
    # The nested for-loop that encapsulates the Discrete Inverse Fourier Series
    for n in range(N):
        for k in range(N):
            x[n] += a[k] * np.exp(1j * k * 2*PI/N * n)
    
    return samples, x
    
def main(func:callable):
    # Calculate the Fourier Coefficients a_k and save them in the array 'a'.
    a = fourier_series(func)
    
    # With the inverse fourier series can be checked if the coefficients are correct, and the original signal can 
    # get plotted as well.
    samples, x = inv_fourier_series(a)
    
    print(f'\nOriginal signal: {x.real}\n')
    print(f'Fourier coefficients: {a}\n\n')
    
    plt.figure()
    plt.title(f'Function: {func.__name__}')
    
    # Creating plots of the real and imaginary parts of the complex coefficients.  
    plt.plot(samples, a.imag, 'C0', label='Imag', alpha=0.3)
    plt.plot(samples, a.real, 'C1', label='Real', alpha=0.3)
    plt.xlabel('n')
    plt.ylabel('x[n]')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
    
    
    
    
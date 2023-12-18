import numpy as np
import matplotlib.pyplot as plt

PI = np.pi


# The class "functions" contains two functions, "simple" and "euler", which return lists of numbers
# and their corresponding values.
class functions():
    def simple():
        """
        The function "simple" returns a list of numbers and the value of N.
        :return: a list of numbers [2, -1, 3, 1] and the value of N which is 4.
        """

        N = 4
        x = [2, -1, 3, 1]
        return x, N

    def euler():
        """
        The function `euler()` returns an array `x` of complex numbers representing the values of Euler's
        formula for `N` points, along with the value of `N`.
        :return: two values: `x` and `N`.
        """
        
        N = 32
        n = np.arange(N)
        x = np.exp(1j*n*2*PI/32)
        return x, N


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
    
    for k in range(N):
        sum = 0
        for n in range(N):            
            sum += (x[n] * np.exp(-1j * k * 2*PI/N * n))
        a[k] = 1/N * sum

    return a


def inv_fourier_series(a):
    """
    The function `inv_fourier_series` calculates the inverse discrete Fourier transform of a given
    sequence `a`.
    
    :param a: The parameter "a" is a list or array of coefficients representing the Fourier series
    :return: two values: "samples" and "x". "samples" is an array containing the indices of the samples,
    and "x" is an array containing the values of the inverse Fourier series.
    """
    
    N = len(a)
    samples = np.arange(N)
    x = np.zeros(N, dtype=complex)
    
    for n in range(N):
        for k in range(N):
            x[n] += a[k] * np.exp(1j * k * 2*PI/N * n)
    
    return samples, x
    

# The `if __name__ == "__main__":` block is used to ensure that the code inside it is only executed
# when the script is run directly, and not when it is imported as a module.
if __name__ == "__main__":
    
    a = fourier_series(functions.euler)
    samples, x = inv_fourier_series(a)
    
    plt.plot(samples, x.imag, 'C0', alpha=0.3)
    plt.plot(samples, x.real, 'C1', alpha=0.3)
    plt.plot(samples, np.abs(x), 'C2')
    plt.show()
    
    
    
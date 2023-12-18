import DFT
import numpy as np
import func


# Declaring constants
PI = np.pi

def func3_2():
    # Periodiek signaal
    x = [2, -4, 1, -2, 3, -2, 2]
    N = len(x)
    
    return x, N

def func3_3():
    # Oneven signaal
    N = 8
    n = np.arange(-N, N)
    x = -2*n * np.cos(n)

    return x, N

def func3_4():
    # Even signaal
    N = 8
    n = np.arange(-N, N)
    x = n**4 * np.cos(n)
    
    return x, N

def func3_5():
    # Harmonisch periodiek signaal
    n = np.arange(0, 64)
    
    x = np.zeros(len(n))
    
    for i in n:
        x[i] = 1 + np.cos(i*PI/32) + np.sin(i*PI/4)
    
    return x, len(n)
    
def func3_6():
    # Reeks eenheidimpulsen
    n = np.arange(64)
    f = func.Delta(n, 5)
    
    return f, len(n)
    
    
    
if __name__ == "__main__":
    DFT.main(func3_2)
    DFT.main(func3_3)
    DFT.main(func3_4)
    DFT.main(func3_5)
    DFT.main(func3_6)
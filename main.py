import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl ; mpl.rcParams['text.usetex'] = True

import func

PI = np.pi

def opdracht_1():
    
    plt.figure("Opdracht 1")
    plt.subplot(221)
    indices = func.Indices(10)
    yData = np.sin((2*PI*indices) / 10)
    plt.stem(indices, yData)
    
    plt.subplot(222)
    indices = func.Indices(31)
    yData = np.sin((6*PI*indices) / 31)
    plt.stem(indices, yData)
    
    plt.subplot(223)
    indices = func.Indices(30)
    yData = np.cos((PI*indices) / 15) + 0.25 * np.sin((4*PI*indices) / 15)
    plt.stem(indices, yData)
    
    plt.subplot(224)
    indices = func.Indices(60)
    yData = np.cos((PI*indices) / 15 + 0.25*PI) + 0.5*np.cos((5*PI*indices)/30 - 0.3*PI)
    plt.stem(indices, yData)
    
    return 0

def opdracht_2():

    indices = func.Indices(10)

    plt.figure("Opdracht 2")
    plt.subplot(121)
    yData = func.Step(indices, 0)
    plt.stem(indices, yData)

    plt.subplot(122)
    yData = func.Delta(indices, 0)
    plt.stem(indices, yData)

    return 0

def opdracht_3():
    
    plt.figure("Opdracht 3")
    plt.title("Plots bij opdracht 3")

    plt.subplot(231)
    plt.title(r"2.a = $e^{\frac{n}{5}}$")
    indices = func.Indices(20)
    yData = np.exp(indices/5)
    plt.stem(indices, yData)
    
    plt.subplot(232)
    plt.title(r"2.b = $5 e^{-\frac{n}{2}} \cdot u[n]$")
    indices = func.Indices(20)
    yData = 5*np.exp(-(indices/2)) * indices[indices]
    plt.stem(indices, yData)

    plt.subplot(233)
    indices = func.Indices(20)
    yData = np.exp(indices/5) * (indices[indices] - 5)
    plt.stem(indices, yData)

    plt.subplot(234)
    indices = func.Indices(20)
    yData = np.exp((1j*2*PI*indices) / 10) * (indices[indices] + 3)
    plt.stem(indices, yData)

    plt.subplot(235)
    indices = func.Indices(20)
    yData = 0.5 * (np.exp((1j*2*PI*indices) / 24) + np.exp((-1j*2*PI*indices) / 24))
    plt.stem(indices, yData)
    
    plt.subplot(236)
    indices = func.Indices(20)
    yData = 1/(2j) * (np.exp((1j*2*PI*indices) / 24) - np.exp((-1j*2*PI*indices) / 24))
    plt.stem(indices, yData)
    
    return 0


def main():
        
    # opdracht_1()
    # opdracht_2()
    opdracht_3()

    plt.show()

    return 0

if __name__ == main():
    main()

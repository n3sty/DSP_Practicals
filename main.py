import numpy as np
import matplotlib.pyplot as plt

PI = np.pi

def opdracht_1(indices):
    
    plt.figure("Opdracht 1")
    plt.subplot(221)
    yData = np.sin((2*PI*indices) / 10)
    plt.stem(indices, yData)
    
    plt.subplot(222)
    yData = np.sin((6*PI*indices) / 31)
    plt.stem(indices, yData)
    
    plt.subplot(223)
    yData = np.cos((PI*indices) / 15) + 0.25 * np.sin((4*PI*indices) / 15)
    plt.stem(indices, yData)
    
    plt.subplot(224)
    yData = np.cos((PI*indices) / 15 + 0.25*PI) + 0.5*np.cos((5*PI*indices)/30 - 0.3*PI)
    plt.stem(indices, yData)
    
    plt.show()
    
    return 0

def opdracht_2(indices):
    return 0

def main():

    size = 10

    indices = np.arange(-size, size + 1)
    
    # opdracht_1(indices)
    opdracht_2(indices)
    
    return 0

if __name__ == main():
    main()

import numpy as np
import matplotlib.pyplot as plt
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
    

    plt.show()
    plt.close("Opdracht 1")

    return 0

def opdracht_2(indices):

    plt.figure("Opdracht 2")
    plt.subplot(121)
    yData = func.Step(indices, 0)
    plt.stem(indices, yData)

    plt.subplot(122)
    yData = func.Delta(indices, 0)
    plt.stem(indices, yData)

    plt.show()
    plt.close("Opdracht 2")

    return 0

def main():
        
    opdracht_1()
    # opdracht_2(indices)
    
    return 0

if __name__ == main():
    main()

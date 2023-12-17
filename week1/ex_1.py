import matplotlib.pyplot as plt
import numpy as np
import func

PI = np.pi


def main():
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



if __name__ == "__main__":
    main()
    
    plt.show()
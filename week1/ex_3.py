import matplotlib.pyplot as plt
import numpy as np
import func

PI = np.pi

def main():
    """
    The main function plots different stem plots for various mathematical functions.
    :return: The function `main()` does not explicitly return anything.
    """
    plt.figure("Plots bij opdracht 3")

    # a
    plt.subplot(231)
    indices = func.Indices(20)
    yData = np.exp(indices/5)
    plt.stem(indices, yData)

    # b
    plt.subplot(232)
    indices = func.Indices(20)
    yData = 5*np.exp(-(indices/2)) * func.Step(indices)
    plt.stem(indices, yData)

    # c
    plt.subplot(233)
    indices = func.Indices(20)
    yData = np.exp(indices/5) * (func.Step(indices - 5))
    plt.stem(indices, yData)

    # d
    plt.subplot(234)
    indices = func.Indices(20)
    yData = np.exp((1j*2*PI*indices) / 10) * (func.Step(indices + 3))
    plt.stem(indices, yData)

    # e
    plt.subplot(235)
    indices = func.Indices(20)
    yData = 0.5 * (np.exp((1j*2*PI*indices) / 24) + np.exp((-1j*2*PI*indices) / 24))
    plt.stem(indices, yData)

    # f
    plt.subplot(236)
    indices = func.Indices(20)
    yData = 1/(2j) * (np.exp((1j*2*PI*indices) / 24) - np.exp((-1j*2*PI*indices) / 24))
    plt.stem(indices, yData)

    return


if __name__ == "__main__":
    main()
    plt.show()
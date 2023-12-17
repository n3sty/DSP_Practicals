import matplotlib.pyplot as plt
import numpy as np
import func


PI = np.pi


def main():
    indices = func.Indices(10)

    plt.figure("Opdracht 2")
    plt.subplot(121)
    yData = func.Step(indices, 0)
    plt.stem(indices, yData)

    plt.subplot(122)
    yData = func.Delta(indices, 0)
    plt.stem(indices, yData)

    return 0

if __name__ == "__main__":
    main()
    
    plt.show()

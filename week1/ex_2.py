import matplotlib.pyplot as plt
import numpy as np
import func


PI = np.pi


def main():
    """
    The main function plots two stem plots using the Step and Delta functions from the func module.
    :return: The main function does not explicitly return anything.
    """
    indices = func.Indices(10)

    plt.figure("Opdracht 2")
    plt.subplot(121)
    yData = func.Step(indices, 0)
    plt.stem(indices, yData)

    plt.subplot(122)
    yData = func.Delta(indices, 0)
    plt.stem(indices, yData)

    return

# The `if __name__ == "__main__":` statement is used to check if the current script is being run
# directly or if it is being imported as a module.
if __name__ == "__main__":
    main()
    
    plt.show()

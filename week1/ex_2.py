import matplotlib.pyplot as plt
import numpy as np
import func

# Constantes verklaren
PI = np.pi


def main():
    """
    The main function plots two stem plots using the Step and Delta functions from the func module.
    :return: The main function does not explicitly return anything.
    """
    
    # Samplepunten genereren
    indices = func.Indices(10)

    # De step en delta functie weergeven door middel van matplotlib, subplots is erg handig voor het vergelijken van
    # meerdere plots in 1 figuur.
    plt.figure("Opdracht 2")
    plt.subplot(121)
    plt.title('Step-functie')
    yData = func.Step(indices, 0)
    plt.stem(indices, yData)
    plt.xlabel('n')
    plt.ylabel('x[n]')

    plt.subplot(122)
    plt.title('Diracdelta-functie')
    yData = func.Delta(indices, 0)
    plt.stem(indices, yData)
    plt.xlabel('n')
    plt.ylabel('x[n]')

    return


if __name__ == "__main__":
    main()
    
    plt.show()

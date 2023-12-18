import matplotlib.pyplot as plt
import numpy as np
import func

# Constantes verklaren
PI = np.pi
ohm_1 = 1/2 * PI
ohm_2 = ohm_1 + 2 * PI

def main():
    """
    The main function plots the imaginary parts of two complex exponential signals.
    :return: None.
    """
    indices = func.Indices(20)

    plt.figure("Opdracht 4")
    
    # Verschillende omega's om te demonstreren dat omega periodiek is met 2 pi.
    yData_1 = np.exp(1j * ohm_1 * indices)
    yData_2 = np.exp(1j * ohm_2 * indices)
    
    plt.subplot(121)
    plt.stem(indices, np.imag(yData_1))
    
    plt.subplot(122)
    plt.stem(indices, np.imag(yData_2))
    
    return


if __name__ == "__main__":
    main()
    
    plt.show()

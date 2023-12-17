import matplotlib.pyplot as plt
import numpy as np
import func

PI = np.pi

def main():
    ohm_1 = 2 * PI
    ohm_2 = 0.5 * PI

    plt.figure()
    indices = func.Indices(50)
    yData_1 = np.exp(1j * ohm_1 * indices)
    yData_2 = np.exp(1j * ohm_2 * indices)
    plt.stem(indices, np.imag(yData_1))
    plt.stem(indices, np.imag(yData_2))
    
    return 0


if __name__ == "__main__":
    main()
    
    plt.show()

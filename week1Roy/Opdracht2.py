import numpy as np
import matplotlib.pyplot as plt

def step_function(n,step=0):
        ydata_a = []
        for i in n:
            if i < step:
                ydata_a.append(0)
            else:
                ydata_a.append(1)
        return ydata_a

def delta_puls(indexwaarden, stap_locatie=0):
    ydata_b = []
    for i in indexwaarden:
        if i == stap_locatie:
            ydata_b.append(1)
        else:
            ydata_b.append(0)
    return ydata_b


if __name__ == "__main__":
    

    #input waarden
    stap_locatie = 0
    indexwaarden = np.arange(-10, 11)

    #a

    plt.figure("Opdracht 2")
    plt.subplot(121)
    plt.stem(indexwaarden, step_function(indexwaarden, stap_locatie))

    #b
    
    plt.figure("Opdracht 2")
    plt.subplot(122)
    plt.stem(indexwaarden, delta_puls(indexwaarden, stap_locatie))

    plt.show()


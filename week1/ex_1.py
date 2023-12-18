import matplotlib.pyplot as plt
import numpy as np


# Het bestand 'func.py' is een zelfgemaakt bestand wat het gebruiken van veelvoorkomende functies gemakkelijk maakt,
# in dit bestand zijn functies zoals de step- of impuls-input makkelijk bereikbaar.
import func

# Op deze manier zorgt het gebruiken van pi voor niet al te veel "clutter".
PI = np.pi

# Deze functie wordt gebruikt om alle hoofdtaken uit te voeren (en ook te groeperen in latere, ingewikkeldere
# opgaven). 
def main():
    """
    The main function plots four different stem plots using different harmonical functions.
    :return: The function main() is returning nothing.
    """

    # Met de matplotlib.pyplot package is het maken van plotjes op een overzichtelijke manier erg gemakkelijk, 
    # en van dezelfde kwaliteit zoals gewend van Matlab. Wanneer de plots gegenereerd zijn, willen de labels nog wel eens overlappen,
    # na het vergroten van het venster is dit probleem verholpen.
    plt.figure("Opdracht 1")
    plt.subplot(221)
    plt.title('Opdracht 1a')
    indices = func.Indices(10)
    yData = np.sin((2*PI*indices) / 10)
    plt.stem(indices, yData)
    plt.xlabel('n')
    plt.ylabel('x[n]')

    plt.subplot(222)
    plt.title('Opdracht 1b')
    indices = func.Indices(31)
    yData = np.sin((6*PI*indices) / 31)
    plt.stem(indices, yData)
    plt.xlabel('n')
    plt.ylabel('x[n]')

    plt.subplot(223)
    plt.title('Opdracht 1c')
    indices = func.Indices(30)
    yData = np.cos((PI*indices) / 15) + 0.25 * np.sin((4*PI*indices) / 15)
    plt.stem(indices, yData)
    plt.xlabel('n')
    plt.ylabel('x[n]')
    
    plt.subplot(224)
    plt.title('Opdracht 1d')
    indices = func.Indices(60)
    yData = np.cos((PI*indices) / 15 + 0.25*PI) + 0.5*np.cos((5*PI*indices)/30 - 0.3*PI)
    plt.stem(indices, yData)
    plt.xlabel('n')
    plt.ylabel('x[n]')
    
    return


# Deze if-statement zorgt ervoor dat de 'main()' alleen uitgevoerd wordt wanneer het bestand als hoofdmodule wordt aangeroepen,
# en niet wanneer deze geïmporteeerd wordt door een ander script.
if __name__ == "__main__":
    main()
    
    # Het plt.show() commando laat alle matplotlib gegenereerde plotjes zien, wanneer plt.show() mist, 
    # worden de plotjes niet zichtbaar. 
    plt.show()
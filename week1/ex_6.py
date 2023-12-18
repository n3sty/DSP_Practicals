import matplotlib.pyplot as plt
import numpy as np
import func

# Constantes verklaren
PI = np.pi


def processor(n, x, sign=1):
    """
        Neemt een aantal samples (n) en een inputsignaal (x[n]) en berekent vervolgens y[n].
        
        De processor volgens de voorgeschreven waarden, de 'sign' parameter is om het uitvoeren van opdracht 6f makkelijker te maken
        toegevoegd, hiermee kan het teken van de functie gemakkelijk worden omgedraaid.
        
        :returns: y_data: de respons van de functie bij een input x[n]
    """
    
    # np.zeros geeft een lijst gevuld met nullen, die vervolgens met 'list comprehension' vervangen kunnen worden door
    # bedoelde waardes.
    index = 0
    y_data = np.zeros(len(n))
    
    for i in n:
        
        if index - 1 < 0:
            y_data[index] = x[index] * func.Step(n)[index]
        else:
            y_data[index] = (sign * -0.8 * y_data[index-1] + x[index]) * func.Step(n)[index]
        
        index += 1
    
    return y_data


# Een aantal verschillende signalen als input en hun bijbehorende respons van de processor.
def opdrachtA():
    
    def input(n):
        return func.Delta(n)
    
    n = np.arange(-10, 30)
    
    yData = processor(n, input(n))
    
    plt.subplot(231)
    plt.title('6a')
    plt.stem(n, yData)
    
    return n, yData

def opdrachtB():
    
    def input(n):
        return func.Delta(n, 5)
    
    n = np.arange(-10, 30)
    
    yData = processor(n, input(n))
    
    plt.subplot(232)
    plt.title('6b')
    plt.stem(n, yData)
    
    return n, yData

def opdrachtC():
    
    def input(n):
        return [func.Delta(n)[i] + func.Delta(n, 5)[i] for i in range(len(n))]
    
    n = np.arange(-10, 30)
        
    yData = processor(n, input(n))
    
    plt.subplot(233)
    plt.title('6c')
    plt.stem(n, yData)    
    
    return n, yData

def opdrachtD():
    
    def input(n):
        return func.Step(n)
    
    n = np.arange(-10, 30)
    
    yData = processor(n, input(n))
    
    plt.subplot(234)
    plt.title('6d')
    plt.stem(n, yData)
    
    print(f'De functie convergeert rond: {yData[-1]}')
    
    return n, yData

def opdrachtE():
    
    def input(n):
        return np.cos(2*np.pi*n/30)
    
    n = np.arange(-10, 60)
    
    yData = processor(n, input(n))
    
    plt.subplot(235)
    plt.title('6e')
    plt.stem(n, yData)
    
    return n, yData

def opdrachtF():
    
    def input(n):
        return np.cos(2*PI * n/30)
    
    n = np.arange(-10, 60)
    
    yData = processor(n, input(n), sign=-1)
    
    plt.subplot(236)
    plt.title('6f')
    plt.stem(n, yData)
    
    return n, yData


def main():
    """
        main() plot alle verkregen signalen in 1 venster. Wederom is gekozen om de assenlabels weg te laten, op de x-as zijn telkens
        de samples ('n') weergegeven, en op de y-as de groottes op die samplepunten ('x[n]').
    
    """
    opdrachtA()
    opdrachtB()
    opdrachtC()
    opdrachtD()
    opdrachtE()
    opdrachtF()
    
    plt.show()
    
    return 0 


if __name__ == "__main__":
    main()
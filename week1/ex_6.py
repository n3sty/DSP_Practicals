import matplotlib.pyplot as plt
import numpy as np
import func

PI = np.pi


def processor(n, x, sign=1):
    
    index = 0
    y_data = np.zeros(len(n))
    
    for i in n:
        
        if index - 1 < 0:
            y_data[index] = x[index] * func.Step(n)[index]
        else:
            y_data[index] = (sign * -0.8 * y_data[index-1] + x[index]) * func.Step(n)[index]
        
        index += 1
    
    return y_data

def opdrachtA():
    
    def input(n):
        return func.Delta(n)
    
    n = np.arange(-10, 30)
    
    yData = processor(n, input(n))
    
    plt.figure("Opdracht A")
    plt.stem(n, yData)
    
    return 0

def opdrachtB():
    
    def input(n):
        return func.Delta(n, 5)
    
    n = np.arange(-10, 30)
    
    yData = processor(n, input(n))
    
    plt.figure("Opdracht B")
    plt.stem(n, yData)
    
    
    return 0

def opdrachtC():
    
    def input(n):
        return [func.Delta(n)[i] + func.Delta(n, 5)[i] for i in range(len(n))]
    
    n = np.arange(-10, 30)
        
    yData = processor(n, input(n))
    
    plt.figure("Opdracht C")
    plt.stem(n, yData)    
    
    return 0

def opdrachtD():
    
    def input(n):
        return func.Step(n)
    
    n = np.arange(-10, 30)
    
    yData = processor(n, input(n))
    
    plt.figure("Opdracht D")
    plt.stem(n, yData)
    
    print(f'De functie convergeert rond: {yData[-1]}')
    
    return 0

def opdrachtE():
    
    def input(n):
        return np.cos(2*np.pi*n/30)
    
    n = np.arange(-10, 60)
    
    yData = processor(n, input(n))
    
    plt.figure("Opdracht E")
    plt.stem(n, yData)
    
    return 0

def opdrachtF():
    
    def input(n):
        return np.cos(2*PI * n/30)
    
    n = np.arange(-10, 60)
    
    yData = processor(n, input(n), sign=-1)
    
    plt.figure("Opdracht F")
    plt.stem(n, yData)


def main():
    
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
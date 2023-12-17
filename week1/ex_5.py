import numpy as np
import func
import matplotlib.pyplot as plt

PI = np.pi

def vraagA():
       
    f = 100                         # Signaalfrequentie
    N = 100*f                       # Samplefrequentie
    m = 20                          # Periodes gevraagd
    
    omega = 2*PI*m/N
    
    indices = func.Indices(N/m)
    yData = np.cos(omega*indices)
    
    plt.figure()
    plt.plot(indices, yData)
    
    return yData
    

def vraagB(data_A):
    
    f = 100                                     # Signaalfrequentie
    N = f * np.array([10, 5, 2, 0.9, 0.8])      # Samplefrequentie
    m = 20                                      # Periodes gevraagd
    o = 0
    colours = ['r', 'g', 'b', 'y', 'm', 'k']

    plt.figure()

    for n in N:      
        indices = func.Indices(n/m)
        
        yData = np.array([])
        
        for i in indices:
            print(i)
            np.concatenate(data_A[i])
                
        print(yData)
        
        plt.plot(indices, yData)
        
                
    
    # plt.figure()
    
    # for n in N:
    #     omega = 2*PI*m/n
    #     yData = np.cos(omega*indices)
        
    #     plt.stem(indices, yData, colours[o])
    #     o += 1
        
    # plt.legend(colours)
    
    plt.show()



def main():
    
    data_A = vraagA()
    vraagB(data_A)
    
    
    return 0



if __name__ == "__main__":
    main()
    
    plt.show()
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from Opdracht1 import differentievergelijking


alfa= np.arange(0.5, 1, 0.1)
for i in alfa:
    coëfficiënten = ([1], [1, -i])
    differentievergelijking(coëfficiënten, 60)

plt.show()

#d:
#Hoe groter alfa hoe groter de amplitude en stap responsie zijn, de impuls responsie duurt langer om uit te doven

#e 

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt


systeem1 = ([1], [1, -1.5, 0.85])
a2 = 1, -1.85230, 0.94833
b2 = np.array([1, -1.90210, 1])
N = 30


system = signal.TransferFunction(systeem1[0], systeem1[1], dt=1)
t, y = signal.dimpulse(system, n=N)


plt.figure()
plt.stem(t, y[0], 'C0')
plt.show()
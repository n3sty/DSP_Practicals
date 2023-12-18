import numpy as np
import matplotlib.pyplot as plt



n = np.arange(-40,40)
omega = 2/5
y_a = np.exp(1j*omega*n)
y_b = np.exp(1j*(omega+2*np.pi)*n)


plt.figure("Opdracht 4")
plt.stem(n, y_a)
plt.stem(n ,y_b, "g")
plt.show()

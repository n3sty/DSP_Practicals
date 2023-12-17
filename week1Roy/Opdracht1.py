import numpy as np
import matplotlib.pyplot as plt

#a
n_a = np.arange(0,10)
y_a = np.sin(2*np.pi*n_a/10)
plt.figure("Opdracht 1")
plt.subplot(221)
plt.stem(n_a,y_a)

#b
n_b = np.arange(0,31)
y_b = np.sin(6*np.pi*n_b/31)
plt.subplot(222)
plt.stem(n_b,y_b)

#c
n_c = np.arange(0, 30)
y_c = np.cos(np.pi*n_c/15) + 0.25*np.sin(4*np.pi*n_c/15)
plt.subplot(223)
plt.stem(n_c,y_c)

#c
n_d = np.arange(0, 60)
y_d = np.cos(np.pi*n_d/15 + 0.25*np.pi) + 0.5*np.cos(5*np.pi*n_d/30 - 0.3*np.pi)
plt.subplot(224)
plt.stem(n_d,y_d)



plt.show()
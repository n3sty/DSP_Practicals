import numpy as np
import matplotlib.pyplot as plt
from Opdracht2 import step_function



#a
n_a = np.arange(-20,20)
y_a = np.exp(n_a/5)

plt.figure("opdracht 3")
plt.subplot(231)
plt.stem(n_a, y_a)

#b
n_b = np.arange(-10,20)
y_b = 5*np.exp(-n_b/2)*step_function(n_b)

plt.subplot(232)
plt.stem(n_b, y_b)

#c
n_c = np.arange(-15,20)
y_c = np.exp(n_c/5)*step_function(n_c-5)

plt.subplot(233)
plt.stem(n_c, y_c)

#d
n_d = np.arange(-20,20)
y_d = np.exp(1j*2*np.pi*n_d/10)*step_function(n_d+3)

plt.subplot(234)
plt.stem(n_d, y_d.real)

#e
n_e = np.arange(-20,20)
y_e = 0.5*(np.exp(1j*2*np.pi*n_e/24) + np.exp(-1j*2*np.pi*n_e/24))

plt.subplot(235)
plt.stem(n_e, y_e.real)

#f
n_f = np.arange(-20,20)
y_f = 0.5*1j*(np.exp(1j*2*np.pi*n_f/24) - np.exp(-1j*2*np.pi*n_f/24))

plt.subplot(236)
plt.stem(n_f, y_f.real)

plt.show()
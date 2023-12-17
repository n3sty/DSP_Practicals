import numpy as np
import matplotlib.pyplot as plt

#a
f = 100     #frequentie signaal
N = 100*f   #Sample frequentie
m = 20      #periode
omega = 2*np.pi*m/N
frequentie = m/N    #
n = np.arange(-10*(1/frequentie), 10*(1/frequentie))
y = np.cos(omega*n)

plt.figure("Opdracht 5")
plt.plot(n, y)
plt.show()

#b
N2 = np.array([10, 5, 2, 0.9, 0.8])*f
n = np.arange(-N2.max()/m, N2.max()/m)
kleurtjes = ["b", "g", "r", "y", "m"]
legenda = ["10", "5", "2", "0,9", "0,8"]
index = [ 0, 1, 2, 3, 4]
for i in index:
    omega = 2*np.pi*m/N2[i]
    y = (np.cos(omega*n))
    plt.figure("Opdracht 5b")
    plt.stem(n, y, kleurtjes[i])

plt.legend(legenda)

plt.show()

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt


def delta_puls(indexwaarden, stap_locatie=0):
    ydata_b = []
    for i in indexwaarden:
        if i == stap_locatie:
            ydata_b.append(1)
        else:
            ydata_b.append(0)
    return ydata_b

def step_function(n,step=0):
        ydata_a = []
        for i in n:
            if i < step:
                ydata_a.append(0)
            else:
                ydata_a.append(1)
        return ydata_a



n = np.arange(0, 60)

def differentie_1(input, samples):
    y = []
    for i in range(len(input)):
        if i-1 < 0:
            y.append(input[i]*step_function(samples)[i])
        elif i-2<0:
            y.append((1.5*y[i-1]+input[i])*step_function(samples)[i])
        else:
            y.append((1.5*y[i-1]-0.85*y[i-2] + input[i]) *step_function(samples)[i])
    return y



plt.figure("Opdracht 1a")
plt.subplot(221)
plt.stem(n, differentie_1(delta_puls(n), n))

plt.subplot(222)
plt.stem(n, differentie_1(step_function(n), n))

def differentie_2(input, samples):
    y = []
    for i in range(len(input)):
        if i-1 < 0:
            y.append(input[i]*step_function(samples)[i])
        elif i-2<0:
            y.append((1.85230*y[i-1]+input[i]-1.90210*input[i-1])*step_function(samples)[i])
        else:
            y.append((1.5*y[i-1]-0.85*y[i-2] + input[i]-1.90210*input[i-1]+input[i-2]) *step_function(samples)[i])
    return y

plt.figure("Opdracht 1b")
plt.subplot(221)
plt.stem(n, differentie_2(delta_puls(n), n))

plt.subplot(222)
plt.stem(n, differentie_2(step_function(n), n))

plt.show()
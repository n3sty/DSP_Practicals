import numpy as np
import matplotlib.pyplot as plt
from Opdracht2 import step_function
from Opdracht2 import delta_puls


samples = np.arange(-5, 50)


def processor(input,samples, minteken=1):
    y = []
    for i in range(len(input)):
        if i-1 < 0:
            y.append(input[i]*step_function(samples)[i])
        else:
            y.append((minteken*-0.8*y[i-1] + input[i]) *step_function(samples)[i])
    return y

#a: Ja hij dempt zichzelf naar 0


DeltaPuls = delta_puls(samples)

plt.figure("Opdracht 6 a en b")
plt.subplot(121)
plt.stem(samples, processor(DeltaPuls, samples) )

#b:Hij is inderdaad tijd-invariant
DeltaPuls2 = delta_puls(samples, 5)

plt.subplot(122)
plt.stem(samples, processor(DeltaPuls2, samples))

#c
DeltaPuls3 =[] 
for i in range(len(DeltaPuls)):
    DeltaPuls3.append(DeltaPuls[i] + DeltaPuls2[i])

plt.figure("Opdracht 6c")
plt.stem(samples, processor(DeltaPuls3, samples))


#d

StapFunctie = step_function(samples)

plt.figure("Opdracht 6d")
plt.stem(samples, processor(StapFunctie, samples))


#e: Als je kijkt naar vraag a en b dan zie je dat de functie uitdoofd 
#   en dus minder invloed op de cosinus krijgt naarmate je meer samples krijgt.

input_x = np.cos(2*np.pi*samples/30)

plt.figure("Opdracht 6e")
plt.subplot(211)
plt.stem(samples, processor(input_x, samples))

#f
plt.subplot(212)
plt.stem(samples, processor(input_x, samples, -1))


#g: e is een hoog doorlaat filter doordat de kleinere amplitudes geooft worden
#   f is een laag doorlaat filter omdat hier de lage amplitudes versterkt worden
plt.show()

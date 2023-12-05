import numpy as np
import func
import matplotlib.pyplot as plt

PI = np.pi

indices = func.Indices(100)

plt.figure()
plt.plot(indices, np.cos(100*indices))
plt.show()


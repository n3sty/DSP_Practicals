from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

alpha = 0.5

num = [1.0]
den = [1.0, -alpha]

sys = signal.TransferFunction(num, den, dt=0.01)

plt.figure("Impulse & Step")
plt.subplot(121)
t_out, y_out = signal.dimpulse(sys, t=np.linspace(0, 1, 5))
plt.stem(t_out, y_out[0])

plt.subplot(122)
t_out, y_out = signal.dstep(sys, t=np.linspace(0, 1, 5))
plt.stem(t_out, y_out[0])

plt.figure("Freq")
w, h = signal.freqz(num, den, include_nyquist=True)
plt.plot(w, abs(h))

plt.show()
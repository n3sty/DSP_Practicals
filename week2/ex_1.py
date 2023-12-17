from scipy import signal 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

plt.style.use("ggplot")


vgl1 = ([1.0], [1.0, -1.5, 0.85])
vgl2 = ([1.0, -1.90210, 1.0], [1.0, -1.85230, 0.94833])

def PlotImpStepAmp(vgl):
    system = signal.TransferFunction(vgl[0], vgl[1], dt=1)
    t_imp, y_imp = signal.dimpulse(system, n=50)
    t_step, y_step = signal.dstep(system, n=80)
    w, H = signal.freqz(vgl[0], vgl[1])



    gs = gridspec.GridSpec(2, 2)

    plt.figure()
    ax = plt.subplot(gs[0, 0])
    plt.stem(t_imp, y_imp[0], 'C0')

    plt.xlabel('Samples (n)')
    plt.ylabel('Impulse response')

    ax = plt.subplot(gs[1, 0])
    plt.stem(t_step, y_step[0], 'C1')

    plt.xlabel('Samples (n)')
    plt.ylabel('Step response')

    ax = plt.subplot(gs[:, 1])
    plt.plot(w, abs(H), 'C2', label='Magnitude')

    plt.legend()
    plt.xlabel('Radians/sample')
    plt.ylabel('Magnitude')


PlotImpStepAmp(vgl1)
PlotImpStepAmp(vgl2)

plt.show()

## De filter van vergelijking 1 is een 
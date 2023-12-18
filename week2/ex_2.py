from scipy import signal
import matplotlib.pyplot as plt
from matplotlib import gridspec
import numpy as np


def DiscreteFunc(vals):
    return np.sin(2*np.pi*vals/60)


def SignalTest(alpha, input=None):
    """
    Plots the impulse, step and amplituderesponse of the transferfunction with a given alpha.
    """
    num = [1.0]
    den = [1.0, -alpha]
    sys = signal.TransferFunction(num, den, dt=0.01)



    # Give the figure a distinguishable title
    plt.figure(f'With alpha: {alpha}')
    
    if type(input) != type(None):
        gc = gridspec.GridSpec(2, 3, hspace=0)
    else:
        gc = gridspec.GridSpec(2, 2, hspace=0)

    # Plots the impulse response
    ax1 = plt.subplot(gc[0, 0])
    plt.title('Impulse response & Step response')
    t_out, y_out = signal.dimpulse(sys, t=np.linspace(0, 1, 5))
    plt.stem(t_out, y_out[0])
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')

    # Plots the step response
    ax2 = plt.subplot(gc[1, 0])
    t_out, y_out = signal.dstep(sys, t=np.linspace(0, 1, 5))
    plt.stem(t_out, y_out[0])
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    
    ax1.sharex(ax2)
    
    # Plots the amplitude response
    plt.subplot(gc[:, 1])
    plt.title('Amplitude response')
    f_out, A_out = signal.freqz(num, den)
    plt.plot(f_out, np.abs(A_out)/(2*np.pi))
    plt.xlabel('Frequency (s^(-1))')
    plt.ylabel('Amplitude')
    
    # Plot the output of the system with a given input
    if type(input) != type(None):
        plt.subplot(gc[:, 2])
        plt.title('Response with a given input')
        y_out = signal.lfilter(num, den, DiscreteFunc(input))
        plt.stem(input, y_out)
        plt.xlabel('Samples (n)')
        plt.ylabel('Amplitude')
    
    


def main():
    """
    Loops through alpha from 0.5 to 0.9 in steps of size: 0.1 and plots the resulting impulse, step, and amplitude 
    response of the signal.
    """

    for alpha in range(5, 9, 1):
        SignalTest(alpha/10)
    
    SignalTest(0.9, np.arange(0, 200, dtype=int))

    plt.show()


if __name__ == "__main__":
    main()



"""
Hoe hoger alpha, hoe dunner de bandbreedte in het frequentiespectrum, maar hoe langer het duurt voor de respons
is uitgedempt in het tijdsdomein. Dit is logisch, want alpha is proportioneel met de invloed van de 'vorige' waarde op de 
nieuwe waarde van de transferfunctie, als deze oude waarde meer aanwezig is in de nieuwe waarde dan neemt de snelheid van
het signaal af in het tijdsdomein natuurlijk.

Ik snap dat de output van het filter een sinusoïde wordt, maar de exacte amplitude van de output uit de transferfunctie
of de alphawaarde halen kan ik denk ik niet.
"""

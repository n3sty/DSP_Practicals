from scipy import signal 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# De a en b's van de beide gegeven vergelijkingen. 
vgl1 = ([1.0], [1.0, -1.5, 0.85])
vgl2 = ([1.0, -1.90210, 1.0], [1.0, -1.85230, 0.94833])

def PlotImpStepAmp(vgl):
    """
        Functie die in één keer de impulsresponsie, stepresponsie en het amplitudespectrum van de meegegeven vergelijking
        bepaalt en plot. Deze functie maakt gebruik van de scipy.signal package, voor verdere documentatie van de specifieke
        functies, kijk op "https://docs.scipy.org/doc/scipy/reference/signal.html"
        
        :returns: None
    """
    
    # Maakt een systeem aan in de vorm van een discrete TransferFunctie (dit is een interne class van scipy.signal)
    system = signal.TransferFunction(vgl[0], vgl[1], dt=1)
    
    # Bepaalt de (discrete) impulsrespons van het systeem, 50 samplepunten weergegeven voor een nette plot (trial-and-error).
    t_imp, y_imp = signal.dimpulse(system, n=50)
    
    # Bepaalt de (discrete) staprespons van het systeem, 80 samplepunten weergegeven voor een nette plot (trial-and-error).
    t_step, y_step = signal.dstep(system, n=80)
    
    # Bepaalt de (discrete) frequentierespontie van het systeem, welke later wordt omgezet naar de amplituderesponsie.
    w, H = signal.freqz(vgl[0], vgl[1])

    # Speciale class van de matplotlib module waarmee figuren makkelijker onderverdeeld kunnen worden in bijzondere subplots.
    gs = gridspec.GridSpec(2, 2)

    plt.figure(f"{vgl}")
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
    
    return

if __name__ == "__main__":
    PlotImpStepAmp(vgl1)
    PlotImpStepAmp(vgl2)
    
    plt.show()


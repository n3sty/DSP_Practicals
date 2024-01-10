import numpy as np

PI = np.pi

class Signal:
    def __init__(self, sample_f, freq=PI, order=5, phase=PI/4):
        
        self.samples = np.arange(0, 20000)
        self.sample_f = sample_f
        
        self.order = order
        self.phase = phase
        self.f = freq
        self.type = type
    
    def constructSignal(self, type):
        
        self.type = type
        
        signal = np.ones(len(self.samples))
        
        if type == "sine":
            for i in range(self.order):
                sine = 1/(i+1) * np.sin(self.f * 1/4*(i+1) * self.samples + self.phase)
                signal = signal * sine
            # signal = signal * 0.5 * np.sin(1/100 * self.samples)
            return signal
        

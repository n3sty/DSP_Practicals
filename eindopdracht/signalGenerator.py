import numpy as np

PI = np.pi

class Signal:
    def __init__(self, freq, samples, offset=0, order=5, phase=PI/4):
        
        self.samples = np.arange(0, samples, 1/freq)
        
        self.offset = offset
        self.order = order
        self.phase = phase
        self.f = freq
    
    def constructSignal(self, type):
        
        self.type = type
        
        signal = np.ones(len(self.samples))
        
        if type == "sine":
            for i in range(self.order):
                sine = 1/(i+1) * np.sin(self.f * 1/4*(i+1) * self.samples)
                if i == 0:
                    signal = signal * sine + self.offset
                else:
                    signal = signal + sine
            return signal
        

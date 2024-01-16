import numpy as np

PI = np.pi

class Signal:
    def __init__(self, sample_f, N, freq=PI, order=5, phase=0):
        
        self.samples = np.arange(0, N)
        self.sample_f = sample_f
        
        self.order = order
        self.phase = phase
        self.f = freq
        self.type = type
        
        self.y = self.constructSignal("sine")
    
    def constructSignal(self, type):
        
        self.type = type
        
        signal = np.ones(len(self.samples))
        
        if type == "sine":
            for i in range(self.order):
                sine = 1/(i+1) * np.sin(self.f/self.sample_f * (i+1)/2 * self.samples + self.phase)
                signal = signal * sine
            # signal = signal * 0.5 * np.sin(1/100 * self.samples)
            return signal
        

"""
    Custom signal class for easy access to certain variables, and to make initialization easier.
"""

import scipy.io
import numpy as np
import os

class Signal():
    def __init__(self, title:str, file:str='signaal.mat'):
        self.title = title      
        self.y = scipy.io.loadmat(f'{os.path.dirname(os.path.realpath(__file__))}/{file}')['sig']
        self.x = np.arange(len(self.y))
        

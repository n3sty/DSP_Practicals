"""
    Custom signal class for easy access to certain variables, and to make initialization easier.
"""

import scipy.io
import numpy as np
import matplotlib.pyplot as plt
import os

class Signal:
    def __init__(self, file:str='signaal.mat'):
        self.y = scipy.io.loadmat(f'{os.path.dirname(os.path.realpath(__file__))}/{file}')['sig']
        

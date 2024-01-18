import os, sys, traceback, scipy.io
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec
from scipy.signal import spectrogram

"""
Variables

Functions:
    - Getting a signal (class maybe)
    - Function for filters
    - Function for windows
    - Function for generating FFT data
    - Function for plotting

Main and errorhandling.
"""

sampleRate = 5000   # Hz
N = 20000           # Samples
dBcutoff = 55       # dB
path = "signaal.mat"

def getSignal():
    global path
    

 
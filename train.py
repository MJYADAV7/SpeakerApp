
from __future__ import division
from LBG import lbg
import numpy as np
from scipy.io.wavfile import read
from MFCC_algorithm import mfcc
import matplotlib.pyplot as plt

import os


#training function to train the speaker in order to carry out speaker recognition
def training(nfiltbank):
    nSpeaker = 5
    nCentroid = 4
    codebooks_mfcc = np.empty((nSpeaker,nfiltbank,nCentroid))
    directory = os.getcwd() + '/train';
    fname = str()

    for i in range(nSpeaker):
        fname = '/s' + str(i+1) + '.wav'
        (fs,s) = read(directory + fname)
        mel_coeff = mfcc(s, fs, nfiltbank)
        codebooks_mfcc[i,:,:] = lbg(mel_coeff, nCentroid)

    return (codebooks_mfcc)
    
    

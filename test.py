
from __future__ import division
import numpy as np
from scipy.io.wavfile import read
from LBG import EUDistance
from MFCC_algorithm import mfcc
from train import training
import sounddevice as sd
import wavio as wv
import os

'''#total number of speakers and filters required
totalspeakers = 5
nfilters = 16
#assigning the location of testing data
directory = os.getcwd() + '/test';
fname = str()
codebooks = training(nfilters)

#counter to count the number of speakers correctly identified
nCorrect_MFCC = 0

'''
#calculating the minimum distance between neighbours
def minDistance(features, codebooks):
    speaker = 0
    distmin = np.inf
    for k in range(np.shape(codebooks)[0]):
        D = EUDistance(features, codebooks[k,:,:])
        dist = np.sum(np.min(D, axis = 1))/(np.shape(D)[0]) 
        if dist < distmin:            
            distmin = dist
            speaker = k
    if(23<distmin<32):
        return "Speaker is Manjeet."
    else:
        return "Speaker is not Manjeet."
    return speaker
    
def testing(filename):
    # total number of speakers and filters required
    totalspeakers = 5
    nfilters = 16
    # assigning the location of testing data
    duration = 5
    freq = 44100
    # Start recorder with the given values of
    # duration and sample frequency
    print("Recording start")

    recording = sd.rec(int(duration * freq), samplerate=freq, channels=1)

    # Record audio for the given number of seconds
    sd.wait()
    # Convert the NumPy array to audio file
    wv.write(filename, recording, freq, sampwidth=2)
    directory = os.getcwd()
    fname = "/"+filename
    codebooks = training(nfilters)
    # counter to count the number of speakers correctly identified
    nCorrect_MFCC = 0
    (fs, s) = read(directory + fname)
    mel_coefs = mfcc(s, fs, nfilters)
    return minDistance(mel_coefs, codebooks)



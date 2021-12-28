# import required libraries
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
# Sampling frequency
import test

def startRecording():
    # Recording duration
    duration = 5
    freq = 44100
    # Start recorder with the given values of
    # duration and sample frequency
    print("Recording start")

    recording = sd.rec(int(duration * freq), samplerate=freq, channels=1)

    # Record audio for the given number of seconds
    sd.wait()
    # Convert the NumPy array to audio file
    wv.write("recording1.wav", recording, freq, sampwidth=2)
    test.testing("recording1.wav")

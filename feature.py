import librosa
import numpy as np

def pooling(y, axis=1):
    return np.sum(y, axis=axis)

def logCompression(y, r):
    logChroma = np.log10(1 + r * np.abs(y))
    return logChroma

def extractChroma(y, sr=22050, w=2048, h=1024):
    chroma = librosa.feature.chroma_stft(y, sr, n_fft=w, hop_length=h)
    return chroma 

import librosa
import numpy as np

def pooling(y, axis=1):
    return np.sum(y, axis=axis)

def logCompression(y, r):
    logChroma = np.log10(1 + r * np.abs(y))
    #print (y.shape)
    #print (logChroma.shape)
    return logChroma

def extractChroma(y, sr=22050, w=2048, h=1024, r=0):
    pitch = np.abs(librosa.stft(y,n_fft=w, hop_length=h))**2
    #pitch = librosa.core.piptrack(y=y, sr=sr, n_fft=w, hop_length=h)[0]
    pitch = librosa.core.piptrack(S=pitch, sr=sr)[0]
    if r > 0:
        pitch = logCompression(pitch, r)


    #chroma = librosa.feature.chroma_stft(y, sr, n_fft=w, hop_length=h)
    chroma = librosa.feature.chroma_stft(S=pitch, sr=sr, n_fft=w, hop_length=h)
    return chroma 

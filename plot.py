import numpy as np
import librosa 
import feature as f
import matplotlib.pyplot as plt

path = '../genres/rock/rock.00000.au'
name = 'rock'
a = librosa.load(path, sr=22050)
#y = librosa.core.piptrack(a[0], sr=22050, n_fft=4096, hop_length=2048)
#y = y[0]

p = plt.figure(figsize=(8,3))
y = f.extractChroma(a[0], sr=22050, r=0)
librosa.display.specshow(np.log2(y), y_axis='chroma', x_axis='time')
p.savefig(name + '0.png')


y = f.extractChroma(a[0], sr=22050, r=100)
librosa.display.specshow(np.log2(y), y_axis='chroma', x_axis='time')
p.savefig(name + '100.png')


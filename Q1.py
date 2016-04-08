import numpy as np
import gtz, librosa
import feature as feat
import matplotlib.pyplot as plt

if __name__ == '__main__':
    clips = gtz.readAllClips(n=1)
    print(len(clips))
    f = feat.extractChroma(clips[0][0]) 
    print(f)
    comp = (feat.logCompression(f, 10))
    plt.figure()
    librosa.display.specshow(f, y_axis='chroma', x_axis='time')
    plt.colorbar()
    plt.tight_layout()
    plt.show()
    librosa.display.specshow(comp, y_axis='chroma', x_axis='time')
    plt.show()

import sys
import gtz
import numpy as np
import feature as feat
import matplotlib.pyplot as plt
import Util as u

def Q1(features):
    for i in range(0, len(features)):
        features[i] = feat.logCompression(features[i], r)
        features[i] = feat.pooling(features[i])
    am = np.argmax(features[0])
    key = gtz.Key_Map[am]
    tup = gtz.Key_List[key]
    print(tup[0])
    print(tup[1])
    print(features[0])
    print(np.argmax(features[0]))
    print(np.mean(features[0]))
    print(features[0][1])
    r1 = np.corrcoef(features[0],tup[0])
    r2 = np.corrcoef(features[0],tup[1])
    print(r1)
    print(r2)

if __name__ == '__main__':
    r = 100
    nClips = 100
    labels = gtz.readAllLabel()    
    features = []    

    base = '../features/'
    paths = [base + 'blues/' , base + 'classical/', base + 'country/', base + 'disco/',
             base + 'hiphop/', base + 'jazz/'     , base + 'metal/'  , base + 'pop/',
             base + 'reggae/', base + 'rock/']
 
    if len(sys.argv) >= 2 and sys.argv[1] == 'r':
        print('read from .csv ...')
        for i in range(0, 10):
            dataset = u.readCSV(paths[i])
            features.extend(dataset)
    else :
        clips = gtz.readAllClips()

        print('start extracting features ...')
        for c in clips:
            features.append(feat.extractChroma(c[0]))

        for i in range(0, 10):
            dataset = features[i*nClips:(i+1)*nClips]
            u.writeCSV(dataset, paths[i])

    #print(features[0])
    #print(feat.logCompression(features[0], r))
    Q1(features) 

    #print(features[0])
    #print(features[0].shape)

    """
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
    """

import sys, math
import gtz
import numpy as np
import feature as feat
import matplotlib.pyplot as plt
import Util as u
import librosa
nClips = 100
r = 1
r_flag = False
csv_flag = False
def matchByGenres(predict, labels):
    for i in range(0, len(predict)/nClips):
        a = i * nClips
        b = (i + 1) * nClips
        o = False
        if i == 1:
            o = True
        if not r_flag:
            #print("accuracy : %f" %(gtz.matching(predict[a:b], labels[a:b], False)))
            print("accuracy : %f, relation : %f" %(gtz.matching(predict[a:b], labels[a:b], False),(gtz.matchRelation(predict[a:b], labels[a:b], False))))
            #print("relation : %f" %(gtz.matchRelation(predict[a:b], labels[a:b], o)))
        else:
            print("relation : %f" %(gtz.matchRelation(predict[a:b], labels[a:b], o)))
    

def method2(features, labels):
    print("method2")
    predict = []
    for i in range(0, len(features)):
        major_tup = gtz.findMajorKey(features[i])
        minor_tup = gtz.findMinorKey(features[i])
        if major_tup[1] > minor_tup[1]:
            predict.append(major_tup[0])
        else :
            predict.append(minor_tup[0])
    
    matchByGenres(predict, labels)

    if not r_flag:
        #print("accuracy : %f" %(gtz.matching(predict, labels)))
        print("accuracy : %f, relation : %f" %(gtz.matching(predict, labels), gtz.matchRelation(predict, labels)))
        #print("relation : %f" %(gtz.matchRelation(predict, labels)))
    else :
        print("relation : %f" %(gtz.matchRelation(predict, labels)))

def method1(features, labels):
    predict = []
    for i in range(0, len(features)):
        k_ind = gtz.getKey(np.argmax(features[i]))
        k_tup = gtz.getKeyTup(k_ind)
        r1 = np.corrcoef(features[i], k_tup[0])[0][1]
        r2 = np.corrcoef(features[i], k_tup[1])[0][1]
        #print("max tonic : %d, key_ind : %d" % (np.argmax(features[i]), k_ind))
        #print("r1 : %f , and %f" %(r1, gtz.corrcoef(features[i], k_tup[0])))
        #print("r2 : %f , and %f" %(r2, gtz.corrcoef(features[i], k_tup[1])))
        
        if r1 > r2:
            predict.append(k_ind)
        else :
            predict.append(k_ind+12)

    matchByGenres(predict, labels)
    if not r_flag:
        #print("accuracy : %f" %(gtz.matching(predict, labels)))
        print("accuracy : %f, relation : %f" %(gtz.matching(predict, labels), gtz.matchRelation(predict, labels)))
        #print("relation : %f" %(gtz.matchRelation(predict, labels)))
    else :    
        print("relation : %f" %(gtz.matchRelation(predict, labels)))

if __name__ == '__main__':
    labels = gtz.readAllLabel()    
    features = []    

    base = '../features/'
    #paths = [base + 'blues/' , base + 'classical/', base + 'country/', base + 'disco/',
    #         base + 'hiphop/', base + 'jazz/'     , base + 'metal/'  , base + 'pop/',
    #         base + 'reggae/', base + 'rock/']
    paths = [base + 'blues/' ,
             base + 'hiphop/', base + 'metal/'  , base + 'pop/',
             base + 'rock/']

    for i in range(0, len(sys.argv)):
        if sys.argv[i] == '-r':
            r = int(sys.argv[i + 1])
            print("set r = %d" %(r))
        elif sys.argv[i] == '-rk':
            r_flag = True
        elif sys.argv[i] == 'r':
            csv_flag = True

    if csv_flag:
        print('read from .csv ...')
        for i in range(0, len(paths)):
            dataset = u.readCSV(paths[i])
            features.extend(dataset)
    else :
        clips = gtz.readAllClips()

        print('start extracting features ...')
        for c in clips:
            x = feat.extractChroma(c[0], r=r)
            #features.append(feat.extractChroma(c[0]))
            features.append(x)

        for i in range(0, len(paths)):
            dataset = features[i*nClips:(i+1)*nClips]
            u.writeCSV(dataset, paths[i])

    #print(features[0])
    #print(feat.logCompression(features[0], r))
    for i in range(0, len(features)):
        features[i] = feat.pooling(features[i])
    
    method1(features, labels) 
    method2(features, labels)
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

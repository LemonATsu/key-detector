import os, time
import librosa
import numpy as np
from numpy import genfromtxt

def ensureDir(directory):
    d = os.path.dirname(directory)
    if not os.path.exists(d):
        os.makedirs(d)

def readClips(path, sr=22050, n=-1):
    list = []
    count = -1
    start = time.clock()

    if n != -1:
        count = 0

    for file in os.listdir(path):
        if file.endswith('.au'):
            print(file)
            list.append(librosa.load(path + file, sr))
            if count == -1:
                continue
            count = count + 1
            if count >= n:
                break

    print('finished reading from path ' + path)
    print('elapsed time : %f' % (time.clock() - start))
    return list

def writeCSV(dataset, path):
    ensureDir(path)
    for i in range(0, len(dataset)):
        fn = path + '%03d' % (i)
        np.savetxt(fn + '.csv', dataset[i])

def readCSV(path):
    dataset = []
    
    for file in os.listdir(path):
        if file.endswith('.csv'):
            print(file)
            data = np.genfromtxt(path + file)
            dataset.append(data)
    return dataset

def readLabel(path):
    labels = []
    for file in os.listdir(path):
        if file.endswith('.txt'):
            print(file)
            f = open(path + file)
            label = int(f.readlines()[0])
            print('label : %d' % (label) )
            f.close()
            labels.append(label)

    return labels


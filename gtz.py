import math
import Util as u
import numpy as np

A_Major  = np.array([0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1], np.int32)
A_Minor  = np.array([1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1], np.int32)
AS_Major = np.array([1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0], np.int32)
AS_Minor = np.array([1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0], np.int32)

B_Major = np.array ([0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1], np.int32)
B_Minor = np.array ([0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1], np.int32)

C_Major  = np.array([1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1], np.int32)
C_Minor  = np.array([1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0], np.int32)
CS_Major = np.array([1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0], np.int32)
CS_Minor = np.array([0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1], np.int32)

D_Major  = np.array([0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1], np.int32)
D_Minor  = np.array([1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0], np.int32)
DS_Major = np.array([1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0], np.int32)
DS_Minor = np.array([0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1], np.int32)

E_Major = np.array([0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1], np.int32)
E_Minor = np.array([1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1], np.int32)

F_Major  = np.array([1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0], np.int32)
F_Minor  = np.array([1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0], np.int32)
FS_Major = np.array([0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1], np.int32)
FS_Minor = np.array([0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1], np.int32)

G_Major  = np.array([1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1], np.int32)
G_Minor  = np.array([1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0], np.int32)
GS_Major = np.array([1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0], np.int32)
GS_Minor = np.array([0, 1, 0, 1, 1, 0, 1, 0, 1, 0 ,1, 1], np.int32)
Key_Map = [3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 1, 2]
Key_List = [(A_Major, A_Minor), (AS_Major, AS_Minor), (B_Major, B_Minor), (C_Major, C_Minor), (CS_Major, CS_Minor),
            (D_Major, D_Minor), (DS_Major, DS_Minor), (E_Major, E_Minor), (F_Major, F_Minor), (FS_Major, FS_Minor),
            (G_Major, G_Minor), (GS_Major, GS_Minor)]

Relative = [21, 22, 23, 12, 13, 14, 15, 16, 17, 18, 19, 20, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 1, 2]
PerfectFifth = [7, 8, 9, 10, 11, 0, 1, 2, 3, 4, 5, 6, 19, 20, 21, 22, 23, 12, 13, 14, 15, 16, 17, 18]

Major_offset = np.array([6.35, 2.23, 3.48, 2.33, 4.38, 4.09, 2.52, 5.19, 2.39, 3.66, 2.29, 2.88])
#Minor_offset = np.array([5.38, 2.60, 3.53, 2.54, 4.75, 3.98, 2.69, 3.34, 3.17, 6.33, 2.68, 3.52])
Minor_offset = np.array([6.33, 2.68, 3.52, 5.38, 2.60, 3.53, 2.54, 4.75, 3.98, 2.69, 3.34, 3.17])

def findKey(y, offset):
    r = -100
    c = -10
    
    for i in range(0, 12):
        t = np.corrcoef(np.roll(y, -i), offset)[0][1]
        if t > r:
            c = i
            r = t
    return (c, r)

def findMajorKey(y):
    tup = findKey(y, Major_offset)
    note = (tup[0] + 3) % 12
    return (note, tup[1])

def findMinorKey(y):
    tup = findKey(y, Minor_offset)
    note = (tup[0] + 3) % 12 + 12
    return (note, tup[1]) 

def matchRelation(pred, labels, output=False):
    total = len(labels)
    count = 0.0
    
    for i in range(0, total):
        if pred[i] == labels[i]:
            count = count + 1.0
            if output:
                print('case 1 : %d %d' %(pred[i], labels[i]))
        elif PerfectFifth[pred[i]] == labels[i]:
            count = count + 0.5
            if output:
                print('case 2 : %d %d' %(PerfectFifth(pred[i]), labels[i]))
        elif Relative[pred[i]] == labels[i]:
            count = count + 0.3
            if output:
                print('case 3 : %d %d' %(Relative[pred[i]], labels[i]))
        elif np.abs(pred[i] - labels[i])== 12 and labels[i] != -1:
            count = count + 0.2
            if output:
                print('case 4 : %d %d' %(np.abs(pred[i]-labels[i]), labels[i]))

    return float(count)/float(total)

def matching(pred, labels, output=False):
    total = len(labels)
    count = 0

    for i in range(0, total):
        if pred[i] == labels[i]:
            count = count + 1
        else :
            if output:
                print("mistake : %d as %d" %(labels[i], pred[i]))
    return float(count) / float(total)

def corrcoef(x, y):
    x_bar = np.mean(x)
    y_bar = np.mean(y)
    
    u = 0
    x_l = 0
    y_l = 0
    for i in range(0, 12):
        xt = x[i] - x_bar
        yt = y[i] - y_bar
        x_l = x_l + xt**2
        y_l = y_l + yt**2
        u = u + xt * yt
    return u / math.sqrt(x_l * y_l)

def getKey(am):
    return Key_Map[am]
def getKeyTup(key):
    return Key_List[key]

def readAllLabel():
    labels = []
    base = '../gtzan_key/genres/'
    paths = [base + 'blues/' , base + 'classical/', base + 'country/', base + 'disco/',
             base + 'hiphop/', base + 'jazz/'     , base + 'metal/'  , base + 'pop/',
             base + 'reggae/', base + 'rock/'] 

    for p in paths:
        labels.extend(u.readLabel(p))
    print len(labels)
    return labels


def readAllClips(sr=22050, n=-1):
    clips = []
    base = '../genres/'
    paths = [base + 'blues/' , base + 'classical/', base + 'country/', base + 'disco/',
             base + 'hiphop/', base + 'jazz/'     , base + 'metal/'  , base + 'pop/',
             base + 'reggae/', base + 'rock/'] 

    for p in paths:
        clips.extend(u.readClips(p, sr, n))

    return clips


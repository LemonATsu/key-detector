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

Key_Map  = {0 : 3, 1 : 4, 2 : 5, 3 : 6, 4 : 7, 5 : 8, 6 : 9, 7 : 10, 8 : 11, 9 : 0, 10 : 1, 11 : 2}
Key_List = [(A_Major, A_Minor), (AS_Major, AS_Minor), (B_Major, B_Minor), (C_Major, C_Minor), (CS_Major, CS_Minor),
            (D_Major, D_Minor), (DS_Major, DS_Minor), (E_Major, E_Minor), (F_Major, F_Minor), (FS_Major, FS_Minor),
            (G_Major, G_Minor), (GS_Major, GS_Minor)]


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


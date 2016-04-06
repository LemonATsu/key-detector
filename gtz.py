import Util as u

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

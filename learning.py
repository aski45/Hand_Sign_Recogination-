import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

# genrate prediction using trained model
def getanswer(testlist):
    preds = clf.predict([testlist])
    return preds        #return prediction to livecam for output

# gathering dataset for training model genrated by train.py
sign = pd.read_csv("alpha.csv")   # reading csv file

features = sign.drop("OUTPUT", axis = 1)
lables = sign["OUTPUT"].copy()

# fiting data to classifier
clf = KNeighborsClassifier()
clf.fit(features , lables)

print("LEARNING SUCCESFULL")
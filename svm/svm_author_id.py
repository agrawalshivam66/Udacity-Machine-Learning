#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
t0 = time()
from sklearn import svm
import array
count=0
features_train = features_train[:len(features_train)//100] 
labels_train = labels_train[:len(labels_train)//100] 
clf = svm.SVC(kernel='rbf', C=10000.0)
clf.fit(features_train, labels_train)
print ("training time:", round(time()-t0, 3), "s")
t0 = time()
for index in range(len(features_test)):
    if(clf.predict(features_test[index].reshape(1, -1))==1):count=count+1
print ("predict time:", round(time()-t0, 3), "s")
print(count)
print(clf.score(features_test, labels_test))
#########################################################

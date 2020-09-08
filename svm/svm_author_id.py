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

# features_train = features_train[:len(features_train)/100]
# labels_train = labels_train[:len(labels_train)/100]


#########################################################
from sklearn.svm import SVC

# from sklearn.model_selection import GridSearchCV

param_grid = {'C' : [10, 100, 1000, 10000], 'kernel': ['linear', 'rbf']}
# clf = GridSearchCV(SVC(), param_grid=param_grid)
# clf.fit(features_train, labels_train)
# clf.predict(features_test)
# print clf.cv_results_

# for i in param_grid['C']:
clf = SVC(kernel='rbf', C=10000)

t0 = time()
clf.fit(features_train, labels_train)
print "Training Time: ", time() - t0

t1  = time()
labels_pred = clf.predict(features_test)
print "Prediction Time: ", time() - t1

from sklearn.metrics import accuracy_score

acc = accuracy_score(labels_test, labels_pred)

print "SVM Accuracy: {}".format(acc)
# print "10: ", labels_pred[10], "26: ", labels_pred[26], "50: ", labels_pred[50]
print len(labels_pred[labels_pred == 1])
#########################################################



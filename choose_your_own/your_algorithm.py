#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
# plt.xlim(0.0, 1.0)
# plt.ylim(0.0, 1.0)
# plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
# plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
# plt.legend()
# plt.xlabel("bumpiness")
# plt.ylabel("grade")
# plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary

from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import accuracy_score


param_d = {'acc': [], 'param_list': []}
for k in range(1,15):
    clf = KNeighborsClassifier(n_neighbors=k, metric="manhattan")
    clf.fit(features_train, labels_train)
    labels_pred = clf.predict(features_test)
    acc = accuracy_score(labels_test, labels_pred)
    param_d['acc'].append(acc)
    param_d['param_list'].append(clf.get_params())
    print "Accuracy: ", acc, "for K= ", k
    if acc > 0.936:
        print clf.get_params()

# print([i for i in range(1,15)])
# print param_d['acc']

plt.plot([i for i in range(1,15)], param_d['acc'])
plt.show()

def main(k, algo, weights, met, p):
    clf = KNeighborsClassifier(n_jobs=-1, n_neighbors=k, algorithm=algo, weights=weights, metric=met, p=p)

    clf.fit(features_train, labels_train)
    labels_pred = clf.predict(features_test)
    metric_used = clf.effective_metric_params_
    par = clf.get_params()
    acc = accuracy_score(labels_test, labels_pred)
    return acc, metric_used, par


# for m in ['euclidean', 'manhattan', 'chebyshev','minkowski']:
#     for i in range(1, 50):
#         for algo in ['ball_tree', 'kd_tree']:
#             for weights in ['uniform', 'distance']:
#                 acc, metric_used, par = main(i, algo, weights=weights, met=m, p=i)
#                 if acc > 0.936:
#                     print "Accuracy: ", acc, "for K= ", i
#                     print "Params: ", par 

# try:
#     prettyPicture(clf, features_test, labels_test)
# except NameError:
#     pass

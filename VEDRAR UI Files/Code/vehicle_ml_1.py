import pandas as pd
import pylab as pl
import numpy as np
import scipy.optimize as opt
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
data = pd.read_csv("vehicle.csv")
data.head(10)
data=data.replace('POOR', 20)
data=data.replace('AVG', 50)
data=data.replace('GOOD', 80)
data = data.dropna()
feature_df = data[['speed', 'sudden brakes', 'overtakes', 'closest Dist.']]
X = np.asarray(feature_df)
X[0:5]
y = np.asarray(data['review'])
y [0:48]
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.2, random_state=4)
print ('Train set:', X_train.shape,  y_train.shape)
print ('Test set:', X_test.shape,  y_test.shape)
from sklearn import svm
clf = svm.SVC(kernel='rbf')
clf.fit(X_train, y_train)
yhat = clf.predict(X_test)
yhat [0:5]
from sklearn import metrics
print("Train set Accuracy: ", metrics.accuracy_score(y_train, clf.predict(X_train)))
print("Test set Accuracy: ", metrics.accuracy_score(y_test, yhat))
print(X_test.shape)
print(X_test)
print(clf.predict([[45,3,4,7]]))

from sklearn import tree
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import Perceptron
import numpy as np

X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']

classifier_tree = tree.DecisionTreeClassifier()
classifier_svm = SVC()
classifier_KNN = KNeighborsClassifier()
classifier_perceptron = Perceptron()

classifier_tree.fit(X,Y)
classifier_svm.fit(X,Y)
classifier_KNN.fit(X,Y)
classifier_perceptron.fit(X,Y)

prediction_tree = classifier_tree.predict(X)
accuracy_tree = accuracy_score(Y, prediction_tree) * 100
print('Accuracy for DecisionTree: {}'.format(accuracy_tree))

prediction_svm = classifier_svm.predict(X)
accuracy_svm = accuracy_score(Y, prediction_svm) * 100
print('Accuracy for SVM: {}'.format(accuracy_svm))

prediction_KNN = classifier_KNN.predict(X)
accuracy_KNN = accuracy_score(Y, prediction_KNN) * 100
print('Accuracy for KNN: {}'.format(accuracy_KNN))

prediction_perceptron = classifier_perceptron.predict(X)
accuracy_perceptron = accuracy_score(Y, prediction_perceptron) * 100
print('Accuracy for Perceptron: {}\n'.format(accuracy_perceptron))

#Selecting classifier with highest accuracy
index = np.argmax([accuracy_svm, accuracy_KNN, accuracy_perceptron])
names = {0:'SVM', 1:'KNN', 2:'Perceptron'}
print('The most accurate classifier is {}!\n'. format(names[index]))
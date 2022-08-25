# Group members:
# Andrew Dillon
# Michael Lewson
# Cole Ternes

import numpy as np
X_train=np.array([[1, 1], [3, 2], [2,4], [3, 4], [2,3]])
y_train=np.array([0,1,1,1,0])

def perceptron(x, y, lr, epochs):
    weights = [1, 1, 1]
    for itr in range(epochs):
        for index in range(len(x)):
            y_predicted = prediction(x[index], weights)
            weights[0] = weights[0] + (lr * (y[index] - y_predicted))
            weights[1] = weights[1] + (lr * (y[index] - y_predicted) * x[index][0])
            weights[2] = weights[2] + (lr * (y[index] - y_predicted) * x[index][1])

    return weights

def prediction(x, weights):
    y_predicted = int(weights[0] + (weights[1]*x[0]) + (weights[2]*x[1]))
    return y_predicted

weight = perceptron(X_train, y_train, lr=0.01, epochs=10000)
y_predicted = []
for index in range(len(X_train)):
    y_predicted.append(prediction(X_train[index], weight))
print(y_predicted)

### check the accuracy on the training data
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

print('Accuracy score: {}'.format(accuracy_score(y_train, y_predicted)))

import os
import numpy as np

def MSE(x,y):
    return np.sum((x-y)**2)

LOSSES = {"MSE": MSE}

class regression:
    def __init__(self, loss = 'MSE'):
        self.loss = LOSSES[loss]
        self.parameters = None
    
    def fit(self, X, y):
        X, y = np.array(X), np.array(y)
        self.parameters = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)
        
    def predict(self, X):
        X = np.array(X)
        return X.dot(self.parameters)
    
    def get_metrics(self, pred, target, reduction = None):
        pred, target = np.array(pred), np.array(target)
        
        if reduction is None:
            return self.loss(pred, target)
        elif reduction == 'mean':
            return np.mean(self.loss(pred, target))
        elif reduction == 'sum':
            return np.sum(self.loss(pred, target))
        else:
            raise ValueError('unknown reduction parameter: {}'.format(reduction))
            
    
        
if __name__ == "__main__":
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    # get shape
    F, N = list(map(int, input().strip('\n').split()))
    
    # get training data
    X, y = [],[]
    for i in range(N):
        data=list(map(float, input().strip('\n').split()))
        X.append([1,] + data[:-1]) # add 1 for the bias term
        y.append(data[-1])
        
    #get number of test samples
    N_test = int(input())
    
    # get test data
    X_test = []
    for i in range(N_test):
        # add 1 for the bias term
        X_test.append([1,] + list(map(float, input().strip('\n').split())))
        
    regr = regression(loss = 'MSE')
    regr.fit(X, y)
    pred = regr.predict(X_test)
    
    for p in pred:
        fptr.write("{}\n".format(round(p, 2)))

# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
import itertools

# Get train data
F, N = list(map(int, input().strip("\n").split()))

X,y = [],[]
for i in range(N):
    row = list(map(float, input().strip("\n").split()))
    X.append(row[:F])
    y.append(row[F])

# Get test data
Ntest = int(input().strip("\n"))
Xtest = []
for i in range(Ntest):
    row = list(map(float, input().strip("\n").split()))
    Xtest.append(row)
    
X, Xtest, y = np.array(X), np.array(Xtest), np.array(y)

 
# define polynomial regression class
class PolyRegr:
    def __init__(self, p):
        self.p = p
        self.params = None
    
    def get_basis(self, X):
        # get the basis function for a pth order polinomial
        basis = lambda x: [1]+[np.prod(i) for i in list(itertools.combinations_with_replacement(x, self.p))]
        Phi = []
        for i,row in enumerate(X):
            Phi.append(basis(row))  
        return np.array(Phi)
            
    def fit(self, X, y):
        # get Phi
        Phi = self.get_basis(X)
        #apply normal equation to get optimal params
        self.params = np.linalg.inv(Phi.T.dot(Phi)).dot(Phi.T).dot(y)
    
    def predict(self, X):
        # get Phi
        Phi = self.get_basis(X)
        #return predictions
        return Phi.dot(self.params)
        
regr = PolyRegr(3)
regr.fit(X, y)
ytest = regr.predict(Xtest)

for yt in ytest:
    print(round(yt, 2))
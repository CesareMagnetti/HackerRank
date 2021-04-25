# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

X = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
Y = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]

muX, muY = sum(X)/len(X), sum(Y)/len(Y)

pearsonCoeff = sum([(X[i]-muX)*(Y[i]-muY) for i in range(len(X))])
pearsonCoeff /= math.sqrt(sum([(X[i]-muX)**2 for i in range(len(X))]))
pearsonCoeff /= math.sqrt(sum([(Y[i]-muY)**2 for i in range(len(Y))]))

print(round(pearsonCoeff, 3)
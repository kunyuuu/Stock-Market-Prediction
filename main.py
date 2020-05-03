import datetime
import numpy as np
import pandas_datareader.data as web
import KNN
import polynomial_linear_regression as PL
import Linear_Regression as LR

start = datetime.datetime(2018, 1, 1)
end = datetime.datetime(2019, 12, 1)

start1 = datetime.datetime(2019, 12, 2)
end1 = datetime.datetime(2019, 12, 5)

#gather data one for training, the other for testing
trainingData = web.DataReader("FB", 'yahoo', start, end)
testData = web.DataReader("FB", 'yahoo', start1, end1)
trainset = trainingData.loc[:,['Adj Close','Volume']]
testset = testData.loc[:,['Adj Close','Volume']]

#preprocess all data, calculate the x variables we want
trainset['HL'] = (trainingData['High'] - trainingData['Low']) / trainingData['Close'] * 1000.0
trainset['CO'] = (trainingData['Close'] - trainingData['Open']) / trainingData['Open'] * 1000.0
testset['HL'] = (testData['High'] - testData['Low']) / testData['Close'] * 1000.0
testset['CO'] = (testData['Close'] - testData['Open']) / testData['Open'] * 1000.0

testData.to_csv("p.csv")
shiftDay = 2

X = np.array(trainset)
M = np.array(testset)
X = X[:-shiftDay]

y = np.array(trainset['Adj Close'].shift(-shiftDay))
y = y[:-shiftDay]

#stimulate the data
KNB = KNN.knn(X,y)
LRM = LR.L(X, y, 0)
PLR = PL.polynomial(X,y)

#print the result for each method's simulation
print("knn             ", "Linear Regression", " Polynomial linear regression")
for i in range(len(M)):
    predictX = KNB.predict(M[i],5)
    predictY = LRM.predict(M[i][0])
    predictZ = PLR.fit(M[i])
    print(predictX, predictY, predictZ)


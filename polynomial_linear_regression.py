import numpy as np

class polynomial:
    def __init__(self, inputx, inputy):
        a = np.zeros(shape=(len(inputx), len(inputx[0])+1))
        t = np.zeros(shape=(len(inputy),1))
        for i in range(len(inputy)):
            m = []
            n = []
            m.append(1)
            n.append(inputy[i])
            for j in range(len(inputx[i])):
                m.append(inputx[i][j])
            a[i] = m
            t[i] = n

        aT = a.transpose()
        b = np.linalg.inv(np.matmul(aT,a))
        #it calculates all coefficient and stores as a matrix
        self.w = np.matmul((np.matmul(b, aT)), t)

    #it predicts the value for given input based on the polynomial linear function
    def fit(self, input):
        result = self.w[0][0]
        for i in range(len(input)):
            result += input[i]*self.w[i+1]
        return result[0]
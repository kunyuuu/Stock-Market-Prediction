import numpy as np

class knn:
    def __init__(self, inputx, inputvalue):
        self.data = inputvalue
        self.value = inputx

    def predict(self, predictD, k):
        distance = []
        #it calculates and stores the difference between given predictD and training set "self.value"
        for i in range(len(self.value)):
            d = 0
            for j in range(len(self.value[0])):
                d += (predictD[j] - self.value[i][j]) ** 2
            distance.append(d)

        s = []
        for m in range(k):
            c = distance.index(min(distance))
            s.append(c)
            distance[c] = np.inf

        result = 0
        for n in range(k):
            result += self.data[s[n]]

        answer = result/k
        return answer

import numpy as np
import matplotlib.pyplot as plt

class L:
    def __init__(self, inputx, inputy, number):
        self.ix = inputx
        self.iy = inputy
        self.n = number
        xtotal = 0
        ytotal = 0
        for i in range(len(inputx)):
            xtotal += inputx[i][number]
            ytotal += inputy[i]

        meanx = xtotal/len(inputx)
        meany = ytotal/len(inputy)

        u = 0
        d = 0
        for j in range(len(inputx)):
            d += (inputx[j][number] - meanx) ** 2
            u += (inputx[j][number] - meanx)*(inputy[j] - meany)

        self.k = u/d
        self.b = meany - self.k*meanx

    #it can use to plot the graph and the linear simulated function f(x)
    def plot(self, rX, rY):
        x = np.linspace(rX,rY)
        y = self.k*x+self.b
        plt.plot(x, y, '-r')
        for k in range(len(self.ix)):
            plt.scatter(self.ix[k][self.n], self.iy[k])
        plt.show()

    #function does the prediction by given x value
    def predict(self, x):
        return self.k*x+self.b

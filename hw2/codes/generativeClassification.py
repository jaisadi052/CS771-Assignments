import numpy as np
import matplotlib.pyplot as plt

Qn = 2 #Give 1 for different sigma case and 2 for same sigma case
part = 2 #Give 1 for part 1 and 2 for part 2

if part == 2:
    data = np.genfromtxt('data/binclassv2.txt',delimiter=',')
else:
    data = np.genfromtxt('data/binclass.txt',delimiter=',')

# Calculates the MLE parameters
def calcMLE(x, pF, nF):
    mup = np.mean(x[pF], axis=0)
    mun = np.mean(x[nF], axis=0)
    k = np.std(x[pF], axis=0)
    sigmap = np.mean(k*k)
    k = np.std(x[nF], axis=0)
    sigman = np.mean(k*k)
    mup.reshape((1, mup.shape[0]))
    mun.reshape((1, mun.shape[0]))

    return np.array([mup, mun]), np.array([[sigmap], [sigman]])

# Will pplot the normal data points
def plotDataPoints(x, y, pF, nF):
    plt.plot(x[pF,0], x[pF,1], 'r*')
    plt.plot(x[nF,0], x[nF,1], 'b*')

# plot decision boundary
# ki, kj are the classes for which decision boundary is to be drawn.
# y, x contains min to max ranges for respective axis
# Qn is for type of boundary send Qn == 2 for same sigma else send Qn ==1
def plotDecisionBoundary(mu, sigma, ki, kj, y, x):
    sigmai = sigma[ki].reshape(())
    sigmaj = sigma[kj].reshape(())

    if Qn == 2:
        plt.title('Same Sigma Part: ' + str(part))
        sigmaj = sigmai
    else:
        plt.title('Different Sigma Part: ' + str(part))

    mui = mu[ki].reshape((mu[ki].shape[0], 1))
    muj = mu[kj].reshape((mu[kj].shape[0], 1))

    X, Y = np.meshgrid(x, y)
    Z1 = (sigmai**(-1*mui.shape[0]/2))*np.exp(((X-mui[0])**2 + (Y-mui[1])**2)/(-2*sigmai))
    Z2 = (sigmaj**(-1*mui.shape[0]/2))*np.exp(((X-muj[0])**2 + (Y-muj[1])**2)/(-2*sigmaj))
    Z = Z1 - Z2
    plt.contour(X, Y, Z, 0)

def main():
    x = data[:,:data.shape[1]-1]
    y = data[:,data.shape[1]-1]
    pF = y>0
    nF = y<0
    x2 = np.arange(np.min(x[:,1]),np.max(x[:,1]),0.05)
    x1 = np.arange(np.min(x[:,0]),np.max(x[:,0]),0.05)

    mu, sigma = calcMLE(x, pF, nF)

    plt.xlabel('x1')
    plt.ylabel('x2')
    plotDataPoints(x, y, pF, nF)
    plotDecisionBoundary(mu, sigma, 0, 1, x2, x1)

    plt.show()


main()

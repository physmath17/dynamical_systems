from runge_kutta_four import *
from numpy import sin, cos, sqrt
import numpy as np
from matplotlib import pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.tri as mtri

#parameters
sigma = 10
rho = 28
beta = 8/3

time = np.arange(0., 100.02, 0.05)
h = 0.02
N = 100/0.05

def plot_result(time, z):
    u = z[:,0]
    v = z[:,1]
    w = z[:,2]
    plt.scatter(u, v)
    plt.show()
    plt.scatter(v, w)
    plt.show()
    plt.scatter(w, u)
    plt.show()
    
# solution to the nonlinear problem
x = np.zeros((int(N)+1,3))

# initial conditions
x0 = 1
y0 = 1
z0 = 1
Y = np.array([x0, y0, z0])
x[0,0] = Y[0]
x[0,1] = Y[1]
x[0,2] = Y[2]

def F(t, Y):
    f = np.array([sigma*(Y[1] - Y[0]), Y[0]*(rho - Y[2]) - Y[1], Y[0]*Y[1] - beta*Y[2]])
    return f

for i in range(1, int(N)+1):
   Y = RK4(time[i], h, Y, F)
   x[i,0] = Y[0]
   x[i,1] = Y[1]
   x[i,2] = Y[2]

# representing the results
#plot_result(time, x)

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(x[:, 0], x[:, 1], x[:, 2])
plt.draw()
# ax.plot_trisurf(x[:, 0], x[:, 1], x[:, 2])
plt.show()

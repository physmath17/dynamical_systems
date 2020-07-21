from runge_kutta_four import *
from numpy import sin, cos, sqrt
import numpy as np
from matplotlib import pyplot as plt
import math

#parameters
k = 9
m = 1
b = 0.002

time = np.arange(0., 10.02, 0.02)
h = 0.02
N = 10/0.02

def plot_result(time, z):
   # axs = plt.subplots(2)
    plt.plot(time, z[:,0])
    a = "(amplitude = 5, b = " + str(b) + ")"
    plt.title("Damped Pendulum Motion: " + a)
    plt.xlabel("time (s)")
    plt.ylabel("angle (rad)")
    plt.grid(True)
    plt.show()
    u = z[:,0]
    v = z[:,1]
    plt.plot(u, v)
    plt.show()
    
# solution to the nonlinear problem
x = np.zeros((int(N)+1,2))

# initial conditions
x0 = 5.
v0 = 0.
Y = np.array([x0, v0])
x[0,0] = Y[0]
x[0,1] = Y[1]

def F(t, Y):
    f = np.array([Y[1], -(k/m)*Y[0] - b*Y[1]])
    return f

for i in range(1, int(N)+1):
   Y = RK4(time[i], h, Y, F)
   x[i,0] = Y[0]
   x[i,1] = Y[1]

# representing the results
plot_result(time, x)



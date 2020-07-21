from runge_kutta_four import *
from numpy import sin, cos
import numpy as np
from matplotlib import pyplot as plt
import math

#parameters
g = 9.81
l = 0.1

time = np.arange(0., 10.02, 0.02)
h = 0.02
N = 10/0.02

def plot_result(time, tht1, tht2):
   # axs = plt.subplots(2)
    plt.plot(time, tht1[:,0])
    plt.plot(time, tht2)
    a = "(initial angle = " + str(initial_angle) + " deg)"
    plt.title("Pendulum Motion: " + a)
    plt.xlabel("time (s)")
    plt.ylabel("angle (rad)")
    plt.grid(True)
    plt.legend(["nonlinear", "linear"], loc = "best")
    plt.show()
    u = tht1[:,0]
    v = tht1[:,1]
    plt.plot(u, v)
    plt.show()
    
# solution to the nonlinear problem
THT1 = np.zeros((int(N)+1,2))

# initial conditions
initial_angle = 45.0
tht0 = math.radians(initial_angle)
w0 = math.radians(0.0)
Y = np.array([tht0, w0])
THT1[0,0] = Y[0]
THT1[0,1] = Y[1]

def F(t, Y):
    f = np.array([Y[1], -(g/l)*sin(Y[0])])
    return f

for i in range(1, int(N)+1):
   Y = RK4(time[i], h, Y, F)
   THT1[i,0] = Y[0]
   THT1[i,1] = Y[1]

# solution to the linear problem
w = np.sqrt(g/l)
THT2 = np.array([tht0 * cos(w*t) for t in time])

# representing the results
plot_result(time, THT1, THT2)



from runge_kutta_four import *
from numpy import sin, cos
import numpy as np
from matplotlib import pyplot as plt
import math

#parameters
mu1 = 5
mu2 = 3
mu3 = 2
mu4 = 1
mu5 = 0.5
mu6 = 0.1
mu7 = 0.01

time = np.arange(0., 30.02, 0.02)
h = 0.02
N = 30/0.02

x1 = np.zeros((int(N) + 1))
x2 = np.zeros((int(N) + 1))
x3 = np.zeros((int(N) + 1))
x4 = np.zeros((int(N) + 1))
x5 = np.zeros((int(N) + 1))
x6 = np.zeros((int(N) + 1))
x7 = np.zeros((int(N) + 1))
dx1 = np.zeros((int(N) + 1))
dx2 = np.zeros((int(N) + 1))
dx3 = np.zeros((int(N) + 1))
dx4 = np.zeros((int(N) + 1))
dx5 = np.zeros((int(N) + 1))
dx6 = np.zeros((int(N) + 1))
dx7 = np.zeros((int(N) + 1))

# initial conditions
z0 = 0.05
x0 = 0.0001
Y = np.array([x0, z0])
x1[0] = Y[0]
x2[0] = Y[0]
x3[0] = Y[0]
x4[0] = Y[0]
x5[0] = Y[0]
x6[0] = Y[0]
x7[0] = Y[0]
dx1[0] = Y[1]
dx2[0] = Y[1]
dx3[0] = Y[1]
dx4[0] = Y[1]
dx5[0] = Y[1]
dx6[0] = Y[1]
dx7[0] = Y[1]

# dynamical system
def F1(t, Y):
    f = np.array([Y[1], (mu1)*(1 - Y[0]**2)*Y[1] - Y[0]])
    return f
    
def F2(t, Y):
    g = np.array([Y[1], (mu2)*(1 - Y[0]**2)*Y[1] - Y[0]])
    return g
    
def F3(t, Y):
    p = np.array([Y[1], (mu3)*(1 - Y[0]**2)*Y[1] - Y[0]])
    return p
    
def F4(t, Y):
    q = np.array([Y[1], (mu4)*(1 - Y[0]**2)*Y[1] - Y[0]])
    return q
    
def F5(t, Y):
    u = np.array([Y[1], (mu5)*(1 - Y[0]**2)*Y[1] - Y[0]])
    return u
    
def F6(t, Y):
    v = np.array([Y[1], (mu6)*(1 - Y[0]**2)*Y[1] - Y[0]])
    return v
    
# solving for the system atdifferent times
for i in range(1, int(N)+1):
   Y = RK4(time[i], h, Y, F1)
   x1[i] = Y[0]
   dx1[i] = Y[1]

Y = np.array([x0, z0])

for i in range(1, int(N)+1):
   Y = RK4(time[i], h, Y, F2)
   x2[i] = Y[0]
   dx2[i] = Y[1]
   
Y = np.array([x0, z0])

for i in range(1, int(N)+1):
   Y = RK4(time[i], h, Y, F3)
   x3[i] = Y[0]
   dx3[i] = Y[1]
   
Y = np.array([x0, z0])

for i in range(1, int(N)+1):
   Y = RK4(time[i], h, Y, F4)
   x4[i] = Y[0]
   dx4[i] = Y[1]
   
Y = np.array([x0, z0])

for i in range(1, int(N)+1):
   Y = RK4(time[i], h, Y, F5)
   x5[i] = Y[0]
   dx5[i] = Y[1]
  
Y = np.array([x0, z0])

for i in range(1, int(N)+1):
   Y = RK4(time[i], h, Y, F6)
   x6[i] = Y[0]
   dx6[i] = Y[1]
   
# plotting the results
plt.plot(x1, dx1)
plt.plot(x2, dx2)
plt.plot(x3, dx3)
plt.plot(x4, dx4)
plt.plot(x5, dx5)
plt.plot(x6, dx6)
plt.legend(["5", "3", "2", "1", "0.5", "0.1"], loc = "best")
plt.show()

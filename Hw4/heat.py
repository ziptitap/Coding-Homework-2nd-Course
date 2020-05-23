import numpy as np
from math import exp

#exact solution
def u0(x):
    return np.exp(-x*x/4)
    
def solution(x, t):
    return 1.0 / np.sqrt(t+1) * exp((-x*x)/(4*(t+1)))
    
mu = 1.0                #a real coefficient called the diffusivity of the medium
T = 2.0                 #a moment of time
L, R = -10.0, 10.0      #Left and right ends

n = int(input("Enter n: "))
m = int(input("Enter m: "))
h = (R - L) / n
tau = T / m

x = np.linspace(L, R, n+1)
t = np.linspace(0.0, T, m+1)
y = np.zeros((m+1, n+1))

#method
d = mu * tau / (h*h)
y[0] = np.vectorize(u0)(x)
for k in range(m):
    for i in range(1, n):
        y[k+1][i] = y[k][i] + d*(y[k][i-1] - 2*y[k][i] + y[k][i+1])

    
vsolution = np.vectorize(solution, excluded=['t'])
u = np.zeros((m+1, n+1))
for k in range(m):
    u[k] = vsolution(x, tau*k)


######################################
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate(k):
    plt.clf()                               #clear figure
    plt.ylim(0,1)                           #y axis limits 
    plt.title("time " + str(tau*k) + "   (" +str(n)+"x"+str(m)+")")         
    plt.plot(x, y[k], label = "Numerical")      #points of numerical solution                       
    plt.plot(x, u[k], label = "Analytical")     #points of analytical solution
    plt.legend()
    
ani = animation.FuncAnimation(plt.figure(0), animate, frames=y.shape[0], interval=100)
ani.save('heat.gif', writer='imagemagick', fps=30)
plt.show() 

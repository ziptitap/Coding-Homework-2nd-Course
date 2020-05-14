import numpy as np
from sweep import sweep

def generateSpline(x, y):    
    n = len(x)-1

    a = np.array([0] + [1]*(n-1) + [0])
    b = np.array([1] + [4]*(n-1) + [1])
    c = np.array([0] + [1]*(n-1) + [0])
    f = np.zeros(n+1)
    
    for i in range(1,n):
        h = x[i+1] - x[i]
        f[i] = 3*(y[i-1] - 2*y[i] + y[i+1]) / (h*h)

    B = sweep(a, b, c, f)
    A = [0] * (n)
    C = [0] * (n)
    D = [0] * (n)
    for i in range(n):
        h = x[i+1] - x[i]
        A[i] = (B[i+1] - B[i])/(3*h)
        C[i] = (y[i+1]-y[i])/h - (B[i+1]+2*B[i]) * h / 3
        D[i] = y[i]
    B = B[:-1]
    return A, B, C, D

def spline_interpol(x, y, z):
    m = len(z)
    n = len(x) - 1
    ans = [0] * m
    A, B, C, D = generateSpline(x, y)

    for i in range(m):
        for j in range(n):
            if x[j] <= z[i] < x[j+1]:
                ans[i] = A[j] * (z[i]-x[j]) ** 3 + B[j] * (z[i]-x[j]) ** 2 + C[j] * (z[i]-x[j]) + D[j]
    return ans

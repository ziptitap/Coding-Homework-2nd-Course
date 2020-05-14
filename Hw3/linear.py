import numpy as np

def generateLine(x, y):
    n = len(x) - 1
    A = [0] * n

    for i in range(n):
        A[i] = (y[i+1] - y[i]) / (x[i+1] - x[i])

    return A

def linear_interpol(x, y, z):
    n = len(x) - 1
    m = len(z)
    ans = [0] * m
    A = generateLine(x,y)

    for i in range(m):
        for j in range(n):
            if x[j] <= z[i] < x[j+1]:
                ans[i] = A[j] * (z[i] - x[j]) + y[j]

    return ans
    

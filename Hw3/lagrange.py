import numpy as np

def phi(i, z, x):
    p = 1
    n = len(x)
    for j in range(n):
        if x[i] != x[j]:
            p *= (z - x[j]) / (x[i] - x[j])
    return p

def lagrange_interpol(x, y, z):
    n = len(x)
    m = len(z)
    ans = [0] * m
   
    for i in range(m):
        for j in range(n):
            ans[i] += y[j] * phi(j, z[i], x) 

    return ans

from math import sqrt
import numpy as np
from math import *
from scipy.linalg import solve
import time

def seidel(A, b):
    n = len(A)
    x_new = np.zeros(n)
    eps = 0.0001            # accuracy of calculations
    t = 1
    while t>eps:
        x = np.copy(x_new)
        x_new = np.zeros(n)
        for i in range(n):
            s = 0
            
        # scalar product of the i-th row (all elements up to the i-th) 
        # of the matrix A and vector x (all elements to the i-th)
            s = np.dot(A[i, 0:i],x_new[:i])
            
        # scalar product of the i-th row (all elements of the (i + 1)-th) 
        # matrix A and vector x (all elements of the (i + 1)-th) 
            s += np.dot(A[i, i+1:], x[i+1:])
            x_new[i] = (b[i] - s) / A[i][i]
            
        # precision calculation - the second norm ||x-x_new||
        x1 = x_new - x
        t = sqrt(np.dot(x1,x1))
        x = x_new

    return x_new
    
def check(A,f,x1):
# calculation using a library function
    start = time.time()
    x = solve(A,f)
    start = time.time() - start
    
    #print("Check: ", x)
    x = abs(x-x1)
# Error
    print("Error: ", np.amax(x))
    return start
    
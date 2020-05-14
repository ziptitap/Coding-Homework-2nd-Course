import numpy as np
import copy
from math import *
import time

def cholesky(A,f):
    A = np.array(A)
    n = len(A[:,0])
    L = copy.deepcopy(A)

    L[0][0] = np.sqrt(A[0][0])
# calculation for the first column of the matrix
    L[:,0] = A[:,0] / L[0][0]
 
    for i in range(1,n):   
        for j in range(i+1):
            t=0
            if i == j:
                l = L[i,0:i]        # one-dimensional array - all elements to the i-th of the i-th row 
                t = np.dot(l,l)     #scalar product (l,l)
                L[i][i] = np.sqrt(A[i][i]-t)
            
            elif i>j:
                t = np.dot(L[i,0:j],L[j,0:j]) 
                L[i][j] = (A[i][j]-t) / L[j][j]
     
    x = forwardTrace(L,f)
    return x              

def forwardTrace(A,f):
    A = np.array(A)
    n = len(A[:, 0])
    x = np.zeros(n)
    for i in range(n):
        t=0
        for j in range(i):
            t+= A[i][j] * x[j]
        x[i] = round((f[i] - t) / A[i][i],8)
    return x 
    
def check(A, f,x1):
# Calculations by library function
    start=time.time()
    A = np.linalg.cholesky(A)
    x = np.linalg.solve(A,f)
    start=time.time()-start
    
    #print("Check result: ", x)

# Error    
    x = abs(x-x1)
    print("Error: ", np.amax(x))
    return start




import numpy as np
import copy
import time

def gaussFunc(A):
    eps = 1e-16
    A = np.array(A)
    n = len(A[:, 0])
    
    for k in range(n):
    # find the maximum of the column
        l = abs(A[:,k])
        max = np.amax(l)
        max_row = np.where(l == max)[0][0]

# if maximum = 0, then an error
        if max < eps:
            raise MyException("Check determinant")

# transposition of the leading element
        if max_row != k:
            b = copy.deepcopy(A[k])
            A[k] = copy.deepcopy(A[max_row])
            A[max_row] = copy.deepcopy(b)

# divide all elements of the line by a diagonal one     
        A[k] = A[k] / A[k][k]
         
# calculation of a triangular matrix
        for i in range(k+1,n):
            b = A[i][k]
            A[i] = A[i] - A[k] * b
            A[i][k] = 0
             
    x = backTrace(A)
    return x


class MyException(Exception):
    def __init__(self, text):
        self.txt = text


def backTrace(A):
    A = np.array(A)
    n = len(A[:, 0])
    x = np.zeros(n)
    x[n-1] = A[n-1][n]
    for i in range(n-2,-1,-1):
        t=0
        for j in range(i+1,n):
            t+= A[i][j] * x[j]
        x[i] = A[i][n] - t
    return x  

# Error
def check(A,f,x1):   
# calculation using a library function
    start = time.time()
    x = np.linalg.solve(A,f)
    start = time.time() - start
    #print("Check result: ", x)
    
    x = abs(x-x1)
    print("Error: ", np.amax(x))
    return start



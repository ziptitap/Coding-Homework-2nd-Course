import numpy as np

def sweep(a,b,c,f):
    n = len(f)
    alpha = np.zeros(n+1)
    beta = np.zeros(n+1)
    x = np.zeros(n+1)
    
    # alpha and beta
    for i in range(n):
        d = a[i] * alpha[i] + b[i]
        alpha[i+1] = - c[i] / d
        beta[i+1] = (f[i] - a[i]*beta[i]) / d

    for i in reversed(range(n)):
        x[i] = alpha[i+1]*x[i+1] + beta[i+1]

    return x[:-1]
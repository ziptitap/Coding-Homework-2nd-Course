import matplotlib.pyplot as plt
import numpy as np
import seidel
import jacob
import time


time1 = [0]; time2 = [0]        # time of my calculations and library function computation time
time11 = [0]; time22 = [0] 

print("\n################# Jacobi Method #################\n")
n0 = n = 100; h = 100           # initial matrix size and step

while np.amax(time1) < 0.1:
    A = np.random.uniform(0,10,(n,n))
    f = np.random.uniform(0,10,(n))
    
# diagonal prevalence
    s = np.sum(np.abs(A), axis = 1)     # sum of all elements of each row
    for i in range(n):
        A[i][i] = A[i][i] + s[i]
    
 # sum of all elements of each row
    start = time.time()
    x = jacob.jacob(A,f)
    time1.append(time.time() - start)
    #print("Result: ", x)
    print("n = ", n)
    
# library function computations
    time2.append(jacob.check(A,f,x))
    print("My time: ",time1[-1])
    print("Numpy time: ",time2[-1],end="\n\n")
    n+=h

print("\n################# Seidel Method #################\n")
n1 = 100; h = 100           # initial matrix size and step
while np.amax(time11) < 0.1:
    A = np.random.uniform(0,10,(n1,n1))
    f = np.random.uniform(0,10,(n1))

# diagonal prevalence
    s = np.sum(np.abs(A), axis = 1)       # sum of all elements of each row
    for i in range(n1):
        A[i][i] = A[i][i] + s[i]

# my calculations 
    start = time.time()
    x = seidel.seidel(A,f)
    time11.append(time.time() - start)
    #print("Result: ", x)
    print("n = ", n1)
    
# library function computations    
    time22.append(seidel.check(A,f,x))
    print("My time: ",time11[-1])
    print("Numpy time: ",time22[-1],end="\n\n")
    n1+=h

l = len(time1)
x = [y for y in range(n0,n+1,h)]        # vector of all matrix sizes
ax1 = plt.subplot(211)
ax2 = plt.subplot(212)
ax1.plot(x,time1, label="My Jacob")      # graph for my calculations
ax1.plot(x,time2,label="Numpy Jacob")    # graph for library function calculations
ax1.plot(x,time11[:l], label="My Seidel")      # graph for my calculations
ax1.plot(x,time22[:l],label="Numpy Seidel")    # graph for library function calculations
ax1.set_xlabel("n")
ax1.set_ylabel("time (sec)")
ax1.legend(bbox_to_anchor=(0., 0., 1.0, 1.0), loc='center left', borderaxespad=0.)   

ax2.plot(x,time11[:l], label="My Seidel")      # graph for my calculations
ax2.plot(x,time1, label="My Jacob")      # graph for my calculations
ax2.set_xlabel("n")
ax2.set_ylabel("time (sec)")
ax2.legend(bbox_to_anchor=(0.5, 0., 0.5, 0.5), loc=0, borderaxespad=0.)   
plt.subplots_adjust(wspace=0.45, hspace=0.45)
plt.savefig("fig.jpg")  
plt.show()
print("\n###############################################\n")


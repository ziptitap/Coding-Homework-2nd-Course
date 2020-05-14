import matplotlib.pyplot as plt
import numpy as np
import seidel
import jacob
import time

def choose():
    print("Choose method:\n1 - Jacob\n2 - Seidel\nq - Quit")
    return input()
    
ch=choose() 
while ch!='q':	
    time1 = [0]; time2 = [0]        # time of my calculations and library function computation time
    if ch == "1":
        print("\n################# Jacob Method #################\n")
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
    elif ch == "2":
        print("\n################# Seidel Method #################\n")
        n0 = n = 300; h = 300           # initial matrix size and step
        while np.amax(time1) < 0.1:
            A = np.random.uniform(0,10,(n,n))
            f = np.random.uniform(0,10,(n))
        
        # diagonal prevalence
            s = np.sum(np.abs(A), axis = 1)       # sum of all elements of each row
            for i in range(n):
                A[i][i] = A[i][i] + s[i]
        
        # my calculations 
            start = time.time()
            x = seidel.seidel(A,f)
            time1.append(time.time() - start)
            #print("Result: ", x)
            print("n = ", n)
            
        # library function computations    
            time2.append(seidel.check(A,f,x))
            print("My time: ",time1[-1])
            print("Numpy time: ",time2[-1],end="\n\n")
            n+=h
    else:
        ch = choose()
        continue
    
    x = [y for y in range(n0,n+1,h)]        # vector of all matrix sizes
    plt.plot(x,time1, label="My time")      # graph for my calculations
    plt.plot(x,time2,label="Numpy time")    # graph for library function calculations
    plt.xlabel("n")
    plt.ylabel("time (sec)")
    plt.legend(bbox_to_anchor=(0.5, 0., 0.5, 0.5), loc=0, borderaxespad=0.)     
    plt.show()
    print("\n###############################################\n")
    ch = choose()

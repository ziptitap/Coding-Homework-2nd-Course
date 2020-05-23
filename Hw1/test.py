import matplotlib.pyplot as plt
import gauss
import cholesky 
import sweep
import numpy
import time

# getting data for the sweep method
def get_data(n):
    data = []
    a = numpy.random.uniform(0, 100, (n))
    c= numpy.random.uniform(0, 100, (n))
    f = numpy.random.uniform(0, 100, (n))
    b = numpy.zeros((n))
    b = a + c + 20
    a[0]=0; c[n-1]=0
    
    # create a matrix for a library function
    data = numpy.zeros((3,n))
    data[2, 0:-1] = a[1:]
    data[1] = b
    data[0, 1:] = c[:-1]
    data = numpy.array(data)
    return a,b,c,f,data

# method selection   
def choose():
    print("Choose method:\n1 - Gauss\n2 - Cholesky\n3 - Sweep\nq - Quit")
    return input()
  
# main cycle    
ch=choose() 
while ch!='q':
    time1 = [0]         # time of my calculations
    time2 = [0]         # library function computation time
    
    # Gauss method
    if ch == "1":
        print("\n################# Gauss Method #################\n")
        n0 = n = 100; h = 100           # initial matrix size and step
        
        # while calculation time is less than a second
        while numpy.amax(time1) < 1:
            print("n = ",n)
            A = numpy.random.uniform(0, 100, (n,n+1))
            # diagonal prevalence
            s = numpy.sum(numpy.abs(A), axis = 1)     # sum of all elements of each row
            for i in range(n):
                A[i][i] = A[i][i] + s[i]
                
            start = time.time()
            x = gauss.gaussFunc(A)
            time1.append(time.time() - start)   # time of my calculations for n*n
            #print("Result: ", x)               # result of my calculations
            
            # library function computation time for size n*n
            time2.append(gauss.check(A[:,:-1],A[:,(len(A[:,0]))],x))
            print("My time: ", time1[-1])
            print("Numpy time: ", time2[-1], end="\n\n")
            n += h            
    
    # cholesky method
    elif ch == "2":
        print("\n############### Cholesky Method ################\n")
        n0 = n = 100; h = 100
        
        # while calculation time is less than a second
        while numpy.amax(time1) < 1:
            print("n = ",n)
            f = numpy.random.uniform(0, 100, (n))
            A = numpy.tril(numpy.random.rand(n, n))
            for i in range(n):
                A[i][i] = 100

            start = time.time()
            x = cholesky.cholesky(A,f)
            time1.append(time.time()-start)
            #print("\nResult: ", x)
            time2.append(cholesky.check(A,f,x))
            print("My time: ", time1[-1])
            print("Numpy time: ", time2[-1], end="\n\n")
            n += h 
            
    # sweep method 
    elif ch == "3":
        print("\n############### Cholesky Method ################\n")
        n0 = n = 10000; h = 30000
        while numpy.amax(time1) < 1:
            print("n = ",n)
            a,b,c,f,A = get_data(n)         # receiving data
            start = time.time()
            x = sweep.sweep(a,b,c,f)
            time1.append(time.time()-start)
            #print("\nResult: ", x)
            time2.append(sweep.check(A,f,x))
            print("My time: ", time1[-1])
            print("Numpy time: ", time2[-1], end="\n\n")
            n += h
            
    else:
        ch = choose()
        continue
    x = [y for y in range(n0,n+1,h)]
    
    ax1 = plt.subplot(211)
    ax2 = plt.subplot(212)

    ax1.plot(x,time1, label="My time")
    ax1.plot(x,time2,label="Numpy time", c='r')
    ax1.legend(bbox_to_anchor=(0.5, 0., 0.5, 0.5), loc=0, borderaxespad=0.)
    ax1.set_xlabel("n")
    ax1.set_ylabel("time (sec)")
    
    ax2.plot(x,time2,label="Numpy time", c ='r')
    ax2.legend(bbox_to_anchor=(0.5, 0., 0.5, 0.5), loc=0, borderaxespad=0.)
    ax2.set_xlabel("n")
    ax2.set_ylabel("time (sec)")
    
    plt.subplots_adjust(wspace=0.45, hspace=0.45)
    plt.savefig("graph.jpg")
    plt.show()
    print("\n###############################################\n")
    ch = choose()


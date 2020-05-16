## Homework 2 - 
### How to run:
```python3 test.py```

After starting, a menu of 4 items will appear:  
    1 - Gauss method
    2 - Cholesky method
    3 - Sweep method
    q - quit

Enter one of the items and the corresponding program starts.

Output data:
    n              - matrix dimension;
    Error          - error (the infinity norm of the difference between my and numpy
                     results ||x_my - x_numpy||); 
    My time        - the time of my calculations for the matrix n*n;
    Numpy time     - the computation time of the library function for the matrix n*n.

The dimension of the matrix increases until the time of my calculations exceeds 
1 seconds. When the time exceeds 1 second, the calculations for the selected 
method stop and a graph is displayed. The graph shows the dependence of the time 
of calculations on the size of the matrix.

After closing the graph, the menu reappears.

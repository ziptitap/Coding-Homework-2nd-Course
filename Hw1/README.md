## Homework 1

### How To Run:
```python3 test.py```

### Files Includes With This Project:
  File          | Description
  ------------- | -------------
  gauss.py      | The program implements the gauss method.
  cholesky.py   | The program implements the cholesky method.
  sweep.py      | The program implements the sweep method.
  test.py       | The program organizes the work of all programs.

### Formulation of the problem:
Compare the solution of SLE (system of linear equations) using 
  1. the Gaussian method of library function np.linalg.solve,
  2. the Cholesky method of library function np.linalg.cholesky,
  3. the sweep method of library function scipy.linalg.solve_banded,

with your own implementation on a random matrix with a diagonal prevalence of 100 x 100, 200 x 200, etc. size. 
  Carry out several experiments until the counting time is less than a second. Build dependency graphs. 


### Design Decisions:



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

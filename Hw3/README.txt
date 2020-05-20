## Homework 3

### Formulation Of The Problem

Given 3 text files with numbers written in columns:
        1. train.dat - values *x0 < x1 <...< x_n*;
        2. train.ans - values *y0 < y1 <...< y_n*;
        3. test.dat - values *z0 < z1<...<zm*.

Required to build 3 different interpolation models *y_{i} = f(x_{i})* on *(x_{i}, y_{i})*:
        1. Linear interpolationn;
        2. Lagrange interpolation;
        3. Spline interpolation. 
        
 and apply them on set of *z_{j}*. Output the result to files.

----------------

#### Linear Interpolation

In mathematics, linear interpolation is a method of curve fitting using linear polynomials to construct new data points within the range of a discrete set of known data points.

Linear interpolation on a set of data points *(x_{0}, y_{0})*, *(x_{1}, y_{1}), ..., (x_{n}, y_{n})* is defined as the concatenation of linear interpolants between each pair of data points. Thus, it is sufficiently to consider the case for two points.

If the two known points are given by the coordinates *(x_{0},y_{0})* and *(x_{1},y_{1})*, the linear interpolant is the straight line between these points. For a value *x* in the interval *(x_{0},x_{1})*, the value y along the straight line is given from the equation of slopes

![Equation](../pics/eq10.png)

which can be derived geometrically from the figure on the right. It is a special case of polynomial interpolation with *n = 1*.

Solving this equation for *y*, which is the unknown value at *x*, gives

![Equation](../pics/eq11.png)

which is the formula for linear interpolation in the interval *(x_{0},x_{1})*, *(x_{0},x_{1})*. Outside this interval, the formula is identical to linear extrapolation.

----------------

#### Lagrange Interpolating Polynomial 

Lagrange Interpolating Polynomial is a method for finding the equation corresponding to a curve having some dots coordinates of it.

Given a set of *(k + 1)* data points *(x_{0},y_{0}), ...,(x_{j},y_{j}), ...,(x_{k},y_{k})* where no two *x_{j}* are the same, the interpolation polynomial in the Lagrange form is a linear combination

![Equation](../pics/eq13.png)

of Lagrange basis polynomials

![Equation](../pics/eq14.jpg)

where *0 &#8804; j &#8804; k*. Note how, given the initial assumption that no two *x_{j}* are the same, then (when *m &#8800; j*) *x_{j}-x_{m} &#8800; 0*, so this expression is always well-defined. The reason pairs *x_{i} = x_{j}* with *y_{i} &#8800; y_{j}* are not allowed is that no interpolation function **L** such that *y_{i} = L(x_{i})* would exist; a function can only get one value for each argument *x_{i}*. On the other hand, if also *y_{i} = y_{j}*, then those two points would actually be one single point.

For all *i &#8800; j*, *l_{j}(x)* includes the term *(x - x_{i})* in the numerator, so the whole product will be zero at *x = x_{i}*:

![Equation](../pics/eq15.jpg)

On the other hand,

![Equation](../pics/eq5.png)

In other words, all basis polynomials are zero at *x = x_{i}*, except *l_{j}(x)*, for which it holds that *l_{j}(x_{j}) = 1*, because it lacks the *(x-x_{j})* term.

It follows that *l_{j}(x_{j}) = y_{j}*, so at each point *x_{j}*, *L(x_{j}) = y_{j} + 0 + 0 + ... + 0 = y_{j}*, showing that *L* interpolates the function exactly.

----------------

### Files Includes With This Project
  File          | Description
  ------------- | -------------
  jacob.py      | The program implements the Jacobi method.
  seidel.py     | The program implements the Gauss-Seidel method.
  test.py       | The program organizes the work of all programs.

----------------

### How To Run
```python3 test.py```

----------------

### Project Overview 

The program runs in turn the methods Jacobi and Seidel. 
During the execution there are output data:

  Output data   | Description
  ------------- | -------------
  n             | Matrix dimension.
  Error         | Error (the infinity norm of the difference between my and numpy.
  My time       | Time of my calculations for the matrix nxn.
  Numpy time    | The computation time of the library function for the matrix nxn.

The dimension of the matrix increases until the time of my calculations exceeds 1 seconds. When the time exceeds 1 second, the calculations for the selected method stop and a graph is displayed. The graph shows the dependence of the time of calculations on the size of the matrix.

Example of running the program `test.py`:

 ![](../pics/ex2.png 'Example of running the program')

Plot:

 ![](result.jpg 'Gauss plot')

----------------



Run:
        python3 interpol.py
        
In this program, calculations are made immediately for three interpolation models.
 
Input data:
        train.dat  - x values
        train.ans  - y values
        test.dat   - points at which the function values should be restored.
        
Output data:
        test_linear.ans     - linear interpolation calculation results (for test.dat points)
        test_lagrange.ans   - lagrange interpolation calculation results (for test.dat points)
        test_spline.ans     - spline interpolation calculation results (for test.dat points)

At the end, 4 graphs are displayed: one for the starting points (x, y), the others
for points obtained as a result of the operation of each interpolation model.

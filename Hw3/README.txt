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
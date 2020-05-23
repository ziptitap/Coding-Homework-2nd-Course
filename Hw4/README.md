## Homework 4

### Formulation Of The Problem

  1. Implement the transport equation:

      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  ![Equation](../pics/eq17.png)

where *C = 1*,    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  ![Equation](../pics/eq18.png)

Analytical solution:     
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ![Equation](../pics/eq19.png).


  2. Implement the heat equation:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ![Equation](../pics/eq21.png)

where  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ![Equation](../pics/eq23.png)

Analytical solution:   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;     ![Equation](../pics/eq24.png)


Output a GIF image of the obtained solution for each equation.

----------------

#### Transport Equation

![Equation](../pics/eq10.png)


![Equation](../pics/eq11.png)


----------------

#### Heat Equation 


![Equation](../pics/eq13.png)

of Lagrange basis polynomials

![Equation](../pics/eq14.png)

![Equation](../pics/eq15.png)


----------------

### Files Includes With This Project
  File              | Description
  -------------     | -------------
  heat.py           | The program implements the heat equation.
  transport.py      | The program implements the transport equation.
  heat1.gif         | The GIF-file to show the implementation of heat equation.
  transfer.gif      | The GIF-file to show the implementation of transport equation.
  
----------------

### How To Run
The heat equation:
```python3 test.py```

The transport equation:
```python3 test.py```

----------------

### Project Overview 
        
The programs works separately. 
 
Input data:

        n  -  amount of steps for x axis;
        m  -  amount of steps for t axis;
        
        
Output data:

  * GIF-file for transport equation:
  
    ![Equation](./transfer1.gif)
    
  * GIF-file for heat equation:
  
    ![Equation](./heat1.gif)


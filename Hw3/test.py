import numpy as np
import matplotlib.pyplot as plt
from spline   import spline_interpol
from linear   import linear_interpol
from lagrange import lagrange_interpol

# read from file
def read_file(name, v):
    f = open(name, 'r')
    for line in f:
        v.append(float(line))    
    f.close()

# write into file
def write_file(name, v):
    m = len(v)
    fans = open(name, 'w')
    for i in range(m):
        fans.write(str(v[i]))
        fans.write('\n')

# plotting    
def pltplt(ax, title, x_data, y_data, xlabel, ylabel, color,size):
    ax.set_title(title)
    ax.scatter(x_data,y_data,marker='o', c=color, s=size)
    ax1.scatter(x_data,y_data,marker='o', c=color, s=size)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    
    
x = [[],[],[]]; j = 0
# read data from files
for i in ['./Data/train.dat', './Data/train.ans', './Data/test.dat']:
    read_file(i, x[j])
    j += 1

ans = [[],[],[]]
# calculation of the results of applying each interpolation model
ans[0] = np.copy(spline_interpol(x[0], x[1], x[2]))         # spline interpolation
ans[1] = np.copy(linear_interpol(x[0], x[1], x[2]))         # linear interpolation
ans[2] = np.copy(lagrange_interpol(x[0], x[1], x[2]))       # lagrange interpolation

j=0
# write results to file
for i in ['./Data/test_spline.ans', './Data/test_linear.ans', './Data/test_lagrange.ans']:
    write_file(i, ans[j])
    j+=1

################# Построение графиков (точки) ################
plt.figure(figsize=(10, 7))
ax1 = plt.subplot(221)
ax2 = plt.subplot(222)
ax3 = plt.subplot(223)
ax4 = plt.subplot(224)

pltplt(ax1, 'Input data (blue marker)', x[0], x[1], '$x$', '$y$', 'b', 55)
pltplt(ax2, 'none', x[0], x[1], '$x$', '$y$', 'b', 55)
pltplt(ax3, 'none', x[0], x[1], '$x$', '$y$', 'b', 55)
pltplt(ax4, 'none', x[0], x[1], '$x$', '$y$', 'b', 55)
pltplt(ax2, 'Spline (green marker)', x[2], ans[0], '$z$', '$y$','g', 40)
pltplt(ax3, 'Linear (yellow marker)', x[2], ans[1], '$z$', '$y$','y',40)
pltplt(ax4, 'Lagrange (red marker)', x[2], ans[2], '$z$', '$y$','r', 40)

plt.subplots_adjust(wspace=0.35, hspace=0.35)
plt.savefig("fig.jpg")
plt.show()


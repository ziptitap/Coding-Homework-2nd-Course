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
def pltplt(ax, title, x_data, y_data, xlabel, ylabel, color, edge_c):
    ax.set_title(title)
    ax.scatter(x_data,y_data,marker='o', c=color, edgecolor=edge_c)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    
    
x = [[],[],[]]; j = 0
# read data from files
for i in ['train.dat', 'train.ans', 'test.dat']:
    read_file(i, x[j])
    j += 1

ans = [[],[],[]]
# calculation of the results of applying each interpolation model
ans[0] = np.copy(spline_interpol(x[0], x[1], x[2]))         # spline interpolation
ans[1] = np.copy(linear_interpol(x[0], x[1], x[2]))         # linear interpolation
ans[2] = np.copy(lagrange_interpol(x[0], x[1], x[2]))       # lagrange interpolation

j=0
# write results to file
for i in ['test_spline.ans', 'test_linear.ans', 'test_lagrange.ans']:
    write_file(i, ans[j])
    j+=1

################# Построение графиков (точки) ################
plt.figure(figsize=(10, 7))
ax1 = plt.subplot(221)
ax2 = plt.subplot(222)
ax3 = plt.subplot(223)
ax4 = plt.subplot(224)

pltplt(ax1, 'Input data', x[0], x[1], '$x$', '$y$', 'b', 'r')
pltplt(ax2, 'Spline', x[2], ans[0], '$z$', '$y$','g', 'r')
pltplt(ax3, 'Linear', x[2], ans[1], '$z$', '$y$','y', 'b')
pltplt(ax4, 'Lagrange', x[2], ans[2], '$z$', '$y$','r', 'b')

plt.subplots_adjust(wspace=0.35, hspace=0.35)
plt.show()


# -*- coding: utf-8 -*-

"""
Q7.2 Plots of resistance against 1/N^2
"""

import matplotlib.pyplot as plt
from numpy import zeros, fabs
import time

def sweep (v, p, q, r, s):
    for i in range (1, len(v) - 1):
        for j in range (1, len(v) - 1):
            c = 0.0
            if i==p and j==q: c = 1.0
            if i==r and j==s: c = -1.0
            v[i, j] = 0.25*(v[i - 1, j] + v[i + 1, j] + v[i, j - 1] + v[i, j + 1] + c)

def calc_dv(N, p, q, r, s):
    """
    Calculate voltage between nodes (p, q) and (r, s)
    in an NxN square lattice.
    """

    v = zeros ((N, N), float)
    dv = 1.0e10
    lastdv = 0
    count = 0
    while (fabs(dv - lastdv) > 1.0e-7 * fabs(dv)):
        lastdv = dv
        sweep (v, p, q, r, s)
        dv = v[p, q] - v[r, s]
        count += 1
        
    #print(" (" + str(p) + ", " + str(q) + ") to (" + str(r) + ", " + str(s) + ") N=" + str(N) + " dv=" + str(dv) + " (count " + str(count) + ")")
    return dv

def plot_graph(dx, dy):      
    """
    Setting N up to 500 makes the program take 20 minutes to run
    """  
    #Nlist = [5, 10, 15, 20, 50, 100, 500]
    #Nlist = [50, 100, 150, 200]
    #Nlist = [50, 60, 80, 120, 500] 
    Nlist = [50, 60, 80, 120, 200] # this takes 4 minutes
    #Nlist = [50, 60, 80, 120] # temp
    mlist = []
    dvlist = []
    
    for N in Nlist:
        # Choose two nodes at centre of lattice
        p = q = int((N - 1)/2)
        r = p + dx
        s = q + dy
        m = 1 / (N*N)
        #m = N
        
        # monitor time taken for NxN lattice
        start = time.time()
        
        dv = calc_dv(N, p, q, r, s)
        
        t = time.time() - start
        mlist.append(m)
        dvlist.append(dv)
        print ("N=" + str(N) + " m=" + str(round(m, 6)) + " dv=" + str(dv) + " (time: " + str(round(t, 1)) + "s)")
        
    print (mlist)
    print (dvlist)
    plt.plot(mlist, dvlist)
    plt.xticks(mlist, Nlist)
    plt.xlabel('1 / N^2')
    plt.ylabel('resistance')
    
t0 = time.time()

# Diagonal nodes A(x, y) to C(x+1, y+1)  
# dv settles at around 0.6365
print('Plotting diagonal nodes')
plt.subplot(2, 1, 1)
plot_graph(1, 1)  
plt.title('Diagonal nodes A to C')

# Adjoining nodes A(x, y) to B(x+1, y)  
# dv settles at around 0.5000
print('Plotting adjoining nodes')
plt.subplot(2, 1, 2)
plot_graph(1, 0) 
plt.title('Adjoining nodes A to B')

plt.subplots_adjust(hspace = 1.0)

plt.savefig('network2.png')
t1 = time.time() - t0
print('Total time elapsed: ' + str(round(t1, 1)) + ' seconds')


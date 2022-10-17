# -*- coding: utf-8 -*-

"""
Q7.4 Measurements between varying nodes
"""

import matplotlib.pyplot as plt
from numpy import zeros, fabs
from math import sqrt
import time

def sweep (v, p, q, r, s, alpha = 0):
    for i in range (1, len(v) - 1):
        for j in range (1, len(v) - 1):
            c = 0.0
            if i==p and j==q: c = 1.0
            if i==r and j==s: c = -1.0
            v[i, j] = (v[i - 1, j] + v[i + 1, j] + v[i, j - 1] + v[i, j + 1] - (alpha*v[i, j]) + c) / (4 - alpha)

def calc_dv(N, p, q, r, s, alpha):
    v = zeros ((N, N), float)
    dv = 1.0e10
    lastdv = 0
    count = 0
    while (fabs(dv - lastdv) > 1.0e-7 * fabs(dv)):
        lastdv = dv
        sweep (v, p, q, r, s, alpha)
        dv = v[p, q] - v[r, s]
        count += 1
    return dv, count

def plot_graph(dx, dy, alpha):      
   
    N = 20  # 20x20 lattice
    p = q = 2   # start at (2, 2) 
    r = p
    s = q
    print ("N=" + str(N) + " alpha=" + str(alpha))
    
    distance_list = []
    dv_list = []
    
    #for i in range(0, 11):   # move 12 places
    while r < N and s < N:  # keep within lattice boundary
        distance = sqrt((r - p)**2 + (s - q)**2)     
        start = time.time()
    
        dv, count = calc_dv(N, p, q, r, s, alpha)
        
        t = time.time() - start
        print(" (" + str(p) + ", " + str(q) + ") to (" + str(r) + ", " + str(s) + ") distance=" + str(distance) + " dv=" + str(dv) + " count=" + str(count) + " (time: " + str(round(t, 2)) +  "s)")
        
        distance_list.append(distance)
        dv_list.append(dv)
        
        r += dx
        s += dy

    plt.plot(distance_list, dv_list)
    plt.xlabel('distance')
    plt.ylabel('resistance')
    plt.title('(' + str(p) + ', ' + str(q) + ') to (' + str(r) + ', ' + str(s) + ')')
    
t0 = time.time()

plot_graph(1, 0, 1.8)   # adjoining movement
plot_graph(1, 1, 1.8)   # diagonal movement

plt.savefig('network4.png')

t1 = time.time() - t0
print('Total time elapsed: ' + str(round(t1, 1)) + ' seconds')

"""
Resistance over distance is an interesting graph.
Resistance initially increases as distance increases.
This is to be expected as the current has to pass through more resistors in series.
But the resistance reaches a peak (usually at around half the width of the lattice)
and then starts to decrease at greater distances.
This is because the current has more paths to choose from and so the
effect of resistors in parallel becomes more prominent.
"""


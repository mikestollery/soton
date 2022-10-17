# -*- coding: utf-8 -*-

"""
Q7.3 Speeding up the program
"""

import matplotlib.pyplot as plt
from numpy import zeros, fabs, arange
import time

def sweep (v, p, q, r, s, alpha):
    for i in range (1, len(v) - 1):
        for j in range (1, len(v) - 1):
            c = 0.0
            if i==p and j==q: c = 1.0
            if i==r and j==s: c = -1.0
            
            # New formula (with alpha)
            v[i, j] = (v[i - 1, j] + v[i + 1, j] + v[i, j - 1] + v[i, j + 1] - (alpha*v[i, j]) + c) / (4 - alpha)
            
def calc_dv(N, p, q, r, s, alpha):
    """
    Calculate voltage between nodes (p, q) and (r, s)
    in an NxN square lattice.
    """

    v = zeros ((N, N), float)
    dv = 1.0e10
    lastdv = 0
    count = 0
    start = time.time()
    while (fabs(dv - lastdv) > 1.0e-7 * fabs(dv)):
        lastdv = dv
        sweep (v, p, q, r, s, alpha)
        dv = v[p, q] - v[r, s]
        count += 1
    t = time.time() - start
    print(" N=" + str(N) + " alpha=" + str(round(alpha, 3)) + " dv=" + str(dv) + " count=" + str(count) + " (time: " + str(round(t, 2)) +  "s)")
    return dv, count

def test_alpha(N, p, q, r, s):
    best_count = 100000000
    best_alpha = -1
    best_dv = -1
    alpha_list = arange(0, 2.0, 0.1)
    count_list = []
    
    # Get dv and count using old method (i.e. when alpha = 0)
    old_dv, old_count = calc_dv(N, p, q, r, s, 0)
    
    for alpha in alpha_list:
        dv, count = calc_dv(N, p, q, r, s, alpha)
        count_list.append(count)
        if count < best_count:
            best_count = count
            best_alpha = alpha
            best_dv = dv
    # Care: check that dv produced by best_alpha is the correct value (old_dv)
    # Note that after alpha=2.0 dv is inaccurate, and higher values cause the program to fail
    # Negative values yield higher counts so we discard those.
    print ("New method: best_dv=" + str(best_dv) + " best_count=" + str(best_count) + " best_alpha=" + str(best_alpha))
    print ("Old method:  old_dv=" + str(old_dv) + "  old_count=" + str(old_count))
    plt.plot(alpha_list, count_list)
    plt.xlabel('alpha')
    plt.ylabel('sweep count')
    
t0 = time.time()

"""
20x20 Lattice

Interestingly, there is no smooth curve to read a minimum value for alpha.
Instead, the shape of the graph varies depending on the granularity of alphas chosen.
E.g. at an interval of 0.1 a minimum count of 43 is found at alpha = 1.8
but an interval of 0.01 reveals a count of 40 at alpha = 1.11

In either case, this is a great improvement on the count of 128
which is produced when alpha = 0 (i.e. using the original formula).

"""
title = 'Diagonal nodes in 20x20 lattice'
print(title)
plt.subplot(4, 1, 1)
test_alpha(20, 9, 9, 10, 10)
plt.title(title)

title = 'Adjoining nodes in 20x20 lattice'
print(title)
plt.subplot(4, 1, 2)
test_alpha(20, 9, 9, 10, 9)
plt.title(title)

"""
Different sized lattices also produce varied graphs
"""
title = 'Diagonal nodes in 12x12 lattice'
print(title)
plt.subplot(4, 1, 3)
test_alpha(12, 5, 5, 6, 6)
plt.title(title)

title = 'Adjoining nodes in 12x12 lattice'
print(title)
plt.subplot(4, 1, 4)
test_alpha(12, 5, 5, 6, 5)
plt.title(title)

plt.subplots_adjust(hspace = 2.0)
plt.savefig('network3.png')

t1 = time.time() - t0
print('Total time elapsed: ' + str(round(t1, 1)) + ' seconds')


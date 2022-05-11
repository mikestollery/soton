# -*- coding: utf-8 -*-

"""
Q7.1 My modified network script 
"""

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
        
    print(" (" + str(p) + ", " + str(q) + ") to (" + str(r) + ", " + str(s) + ") N=" + str(N) + " dv=" + str(dv) + " (count " + str(count) + ")")
    return dv

t0 = time.time()

# Assumes current of 1 amp between sample nodes
# therefore resistance = dv

print('Diagonal nodes A(x, y) to C(x+1, y+1)')
dv12ac = calc_dv(12, 5, 5, 6, 6) 
dv5ac = calc_dv(5, 1, 1, 2, 2) 
dv10ac = calc_dv(10, 4, 4, 5, 5) 
dv15ac = calc_dv(15, 6, 6, 7, 7) 
dv20ac = calc_dv(20, 9, 9, 10, 10) 
#print("dv12ac=" + str(dv12ac))
"""
At N=20, dv converges at around 0.6336
"""

print('Adjoining nodes A(x, y) to B(x+1, y)')
dv12ab = calc_dv(12, 5, 5, 6, 5) 
dv5ab = calc_dv(5, 1, 1, 2, 1) 
dv10ab = calc_dv(10, 4, 4, 5, 4) 
dv15ab = calc_dv(15, 6, 6, 7, 6) 
dv20ab = calc_dv(20, 9, 9, 10, 9) 
#print("dv12ab=" + str(dv12ab))
"""
At N=20, dv converges at around 0.4985
"""

t1 = time.time() - t0
print('Time elapsed: ' + str(round(t1, 1)) + ' seconds')



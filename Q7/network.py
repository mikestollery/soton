# -*- coding: utf-8 -*-

"""
7.2.1 The iterative solution of the equations
Original network script from Blackboard
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
N = 5
v = zeros ((N, N), float)
p = q = int((len(v) - 1)/2)
r = s = p + 1
dv = 1.0e10
lastdv = 0
count = 0

t0 = time.time()

while (fabs(dv - lastdv) > 1.0e-7 * fabs(dv)):
    lastdv = dv
    sweep (v, p, q, r, s)
    dv = v[p, q] - v[r, s]
    count += 1
    print(count, dv)

t1 = time.time() - t0
print('Time elapsed: ' + str(round(t1, 1)) + ' seconds')

import matplotlib. pyplot as plt

plt.figure (figsize=(8, 8)) # square plot for square grid
plt.contour(v)

#print(v)
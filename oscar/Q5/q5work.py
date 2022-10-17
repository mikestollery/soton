#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from numpy import zeros, random
m = zeros(10, int)
for i in range (1000):
    n = random . randint(10)
    m[n] = m[n] + 1
print (m)

"""
Q5.1
1000 random integers in the range 0-9 are created.
A count of each of these random integers is stored in the array m.
For example if 7 is produced 92 times, on completion of the loop m[7] will be 92.
At the end is printed a list of the counts of each of the random integers, e.g.
[113  87  95 106 104 107 105  87 102  94]

Q5.2
A large number is needed in order to produce a fairly even spread of integers.
"""


import matplotlib.pyplot as plt
plt.bar( range (10), m, width = 1, align = 'center')
plt.xticks (range (10))

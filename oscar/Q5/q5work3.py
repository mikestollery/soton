#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
5.3
Random floats in range 0 to 0.99999999
Second version computing the bin number.
"""

from numpy import zeros, random
m = zeros(10, int)
for i in range (1000):
    x = random . random()
    k = int(10 * x)
    m[k] = m[k] + 1
print (m)

import matplotlib.pyplot as plt
plt.bar( range (10), m, width = 1, align = 'center')

"""
The distribution of random numbers looks similar to the 'if' method.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
5.3
Random floats in range 0 to 0.99999999
First version using the 'if' method.
"""

from numpy import zeros, random
m = zeros(10, int)
for i in range (1000):
    x = random . random()
    if 0.0 <= x and x < 0.1: m[0] = m[0] + 1
    if 0.1 <= x and x < 0.2: m[1] = m[1] + 1
    if 0.2 <= x and x < 0.3: m[2] = m[2] + 1
    if 0.3 <= x and x < 0.4: m[3] = m[3] + 1
    if 0.4 <= x and x < 0.5: m[4] = m[4] + 1
    if 0.5 <= x and x < 0.6: m[5] = m[5] + 1
    if 0.6 <= x and x < 0.7: m[6] = m[6] + 1
    if 0.7 <= x and x < 0.8: m[7] = m[7] + 1
    if 0.8 <= x and x < 0.9: m[8] = m[8] + 1
    if 0.9 <= x and x < 1.0: m[9] = m[9] + 1
print (m)

import matplotlib.pyplot as plt
plt.bar( range (10), m, width = 1, align = 'center')
#plt.xticks (range (10.0))

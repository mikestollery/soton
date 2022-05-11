#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Q5.4
"""

from numpy import zeros, random, arange
import matplotlib.pyplot as plt

m = zeros(10, int)
for i in range (1000):
    x = random . random()
    k = int(10 * x)
    m[k] = m[k] + 1
print (m)

plt.bar(arange(0, 1, 0.1), m, width = 0.1)
plt.savefig("q5work4.png")


"""
Uses arange from numpy to produce the range
Image file is saved in same folder as python script.
"""
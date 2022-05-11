#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Section 5.4 - Averages of random numbers
Sample code given in worksheet
"""

from math import exp
from numpy import arange
import matplotlib.pyplot as plt

x = arange (0, 10.1, 0.1)
y = [2 * xi * exp(-xi) for xi in x]
z = [xi * xi * exp(-xi) for xi in x]
print(x)
print(y)
print(z)
plt.subplot(2, 1, 1)
plt.plot(x, y)
#plt.xlabel("x-axis")
plt.subplot(2, 1, 2)
plt.plot(x, z)
#plt.subplots_adjust( hspace = 0.2, bottom = 0.3)
plt.show()
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from math import sqrt, sin, pi

"""
45 deg = pi/4 = 0.785398 rad
cos(45) = 1/sqrt(2) = 0.7071
"""

def f4(x):
    # new integrand for 4.6
    alpha = pi/4  # 45 deg (0.785398)
    return 1 / (sqrt(1 - (sin(alpha/2)**2 * sin(x)**2)))

f4v = np.vectorize(f4)
x = np.arange(-pi, pi, 0.1)
plt.plot(x, f4v(x))
plt.show()

"""
This can be plotted within any range.
"""
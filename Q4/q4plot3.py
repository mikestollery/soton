# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from math import sqrt, cos, pi

"""
45 deg = pi/4 = 0.785398 rad
cos(45) = 1/sqrt(2) = 0.7071
"""

def f3(x):
    # integrand of 4.5 (pendulum)
    alpha = pi/4  # 45 deg (0.785398)
    return 1 / (sqrt(cos(x) - cos(alpha)))

f3v = np.vectorize(f3)
# x = np.arange(-0.7853, 0.812, 0.1)  # outer limits of range
x = np.arange(-0.7, 0.7, 0.1)  # limits that show shape of curve
plt.plot(x, f3v(x))
plt.show()

"""
This reports a math domain error if the limits are set beyond -0.7853 and +0.812
Possibly because it goes to infinity?  Check this mathematically.
"""

print("Done.")
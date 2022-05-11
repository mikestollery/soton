# -*- coding: utf-8 -*-

#import matplotlib.pyplot as plt
#import numpy as np
from math import sqrt, sin, pi, fabs

"""
trap0 and trap1 copied from q4work.py
They could be put in a separate file and imported.
"""

def trap0 (f, a, b, n):
    h = float(b - a)/n
    s = 0.5*(f(a) + f(b))
    for i in range (1, n):
        s = s + f(a + i*h)
    return s*h


def trap1(f, a, b, delta, maxtraps = 512):
    n = 8
    inew = trap0 (f, a, b, n)
    iold = -inew # make sure we do not terminate immediately
    while (fabs(inew - iold) > delta * fabs(inew)):
        iold = inew
        n = 2 * n
        if n > maxtraps:
            print (" Cannot reach requested accuracy with", \
                   maxtraps, " trapezia")
            return
        inew = trap0(f, a, b, n)
    return inew



"""
f4 copied from q4plot4.py
"""

def f4(x):
    # new integrand for 4.6 (pendulum)
    alpha = pi/4  # 45 deg (0.785398)
    return 1 / (sqrt(1 - (sin(alpha/2)**2 * sin(x)**2)))

"""
f4v = np.vectorize(f4)
x = np.arange(-pi, pi, 0.1)
plt.plot(x, f4v(x))
plt.show()
"""

delta = 1.0e-7
area = trap1(f4, -pi, pi, delta)

print ("4.2: delta=" + str(delta) + " area=" + str(area))


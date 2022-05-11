# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)


def f1 (x):
    # integrand of 4.1
    return (x**4 * (1 - x)**4) / (1 + x**2)


"""
t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure()
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()


ta1 = np.arange(0.0, 1.0, 0.1)
ta2 = np.arange(0.0, 1.0, 0.02)
plt.subplot(212)
plt.plot(ta1, f1(ta1), 'bo', ta2, f(ta2), 'k')
"""

def quad(x):
    return x**2

quad1 = np.arange(-0.2, 1.2, 0.01)
plt.plot(quad1, f1(quad1))
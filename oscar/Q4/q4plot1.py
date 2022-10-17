# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

def f1 (x):
    # integrand of 4.1
    return (x**4 * (1 - x)**4) / (1 + x**2)

t1 = np.arange(-0.2, 1.2, 0.01)
plt.plot(t1, f1(t1))
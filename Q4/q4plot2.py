# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from math import e

def f2 (x):
    # integrand of 4.4
    return e**(-x**2)

t2 = np.arange(-5, 5, 0.1)
plt.plot(t2, f2(t2))
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Section 5.5.1 - Gaussian random numbers
Code for Q5.7
"""

import numpy as np
import matplotlib.pyplot as plt





mu, sigma = 0, 0.1 # mean and standard deviation
s = np.random.normal(mu, sigma, 1000)

abs(mu - np.mean(s))

abs(sigma - np.std(s, ddof=1))

count, bins, ignored = plt.hist(s, 30, density=True)

plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
               np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
         linewidth=2, color='r')
plt.show()
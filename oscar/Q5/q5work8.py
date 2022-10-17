#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Section 5.5.1 - Gaussian random numbers
Code for Q5.7
"""

from numpy import random

import matplotlib.pyplot as plt
import seaborn as sns

x = random.normal(size=1000)

print(x)

sns.distplot(x, hist = False)

plt.show()
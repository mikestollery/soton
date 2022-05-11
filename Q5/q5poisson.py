#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Section 5.5.2 - Poisson random numbers
Code for Q5.8
"""

from math import ceil
from numpy import arange, zeros, random
import matplotlib.pyplot as plt

# parameters
mean = 15
sample_size = 100000
bin_width = 1
bin_min = 0  # all values lower than this go in the first bin [0]
bin_max = 30   # all values greater than this go in the last bin [bin_size -1]
 
# care must be taken to ensure that very few values fall outside bin_min to bin_max

# this time bin_size is twice the previous size to accommodate negative values
bin_size = int((bin_max - bin_min) / bin_width )
bin_range = arange(bin_min, bin_max, bin_width)

def bin_index(value):
    idx = ceil((value - bin_min) / bin_width)
    if idx <= 0:
        return 0    # lowest bin
    elif idx > bin_size - 1:
        return bin_size - 1 # highest bin   
    return idx
    
def bin_value(idx):
    # inverse of bin_index
    # returns a value that appears in this bin index
    return round(idx * bin_width + bin_min, 1)

def test_bin_index():
    for v in bin_range:
        idx = bin_index(v)
        print (str("{:.2f}".format(v)) + ' ==> ' + str(idx))
        
def test_bin_value():
    for idx in range(0, bin_size):
        value = bin_value(idx)
        print(str(idx) + " --> " + str(value))

#test_bin_index()
#test_bin_value()
    
gbin = zeros(bin_size, int) 

for i in range(sample_size):
    value = random.poisson(mean)
    idx = bin_index(value)
    gbin[idx] = gbin[idx] + 1
        
    #print("i=" + str(i) + " value=" + str(value) + " idx=" + str(idx)) # testing

x = arange (0, bin_size) # range of bins
xt = [bin_value(idx) for idx in x] # to display random number values on x-axis

font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 22}

plt.clf()
plt.rc('font', **font)

plt.plot(x, gbin)
plt.xticks(x, xt)
plt.title('Poisson random numbers')
plt.xlabel('Bins')
plt.ylabel('Count')

#plt.show()
plt.savefig("poisson_random_numbers.png")

"""
Q5.8
The distribution shown in the output file
poisson_random_numbers.png
shows there to be a peak at around 15.
"""




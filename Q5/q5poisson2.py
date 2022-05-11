#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Section 5.5.2 - Poisson random numbers
Code for Q5.9
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
    
# initialisation of bins for means of 2, 4, 6 and 8
bin2 = zeros(bin_size, int) 
bin4 = zeros(bin_size, int) 
bin6 = zeros(bin_size, int) 
bin8 = zeros(bin_size, int) 

for i in range(sample_size):
    value2 = random.poisson(2)
    value4 = random.poisson(4)
    value6 = random.poisson(6)
    value8 = random.poisson(8)
    idx2 = bin_index(value2)
    idx4 = bin_index(value4)
    idx6 = bin_index(value6)
    idx8 = bin_index(value8)
    bin2[idx2] += 1
    bin4[idx4] += 1
    bin6[idx6] += 1
    bin8[idx8] += 1
        
    #print("i=" + str(i) + " value=" + str(value) + " idx=" + str(idx)) # testing

x = arange (0, bin_size) # range of bins
xt = [bin_value(idx) for idx in x] # to display random number values on x-axis

font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 22}

plt.clf()
plt.rc('font', **font)

plt.subplot(4, 1, 1)
plt.plot(x, bin2)
plt.xticks(x, xt)
plt.title('Poisson distribution for mean of 2')
plt.xlabel('Bins')
plt.ylabel('Count')


plt.subplot(4, 1, 2)
plt.plot(x, bin4)
plt.xticks(x, xt)
plt.title('Poisson distribution for mean of 4')
plt.xlabel('Bins')
plt.ylabel('Count')

plt.subplot(4, 1, 3)
plt.plot(x, bin6)
plt.xticks(x, xt)
plt.title('Poisson distribution for mean of 6')
plt.xlabel('Bins')
plt.ylabel('Count')

plt.subplot(4, 1, 4)
plt.plot(x, bin8)
plt.xticks(x, xt)
plt.title('Poisson distribution for mean of 8')
plt.xlabel('Bins')
plt.ylabel('Count')

plt.subplots_adjust( hspace = 0.5)
#plt.show()
plt.savefig("poissons_of_several_means.png")

"""
Q5.10
At low means the peak is "squashed" towards the y-axis.
Higher means allow the curve to spread out more evenly.
"""




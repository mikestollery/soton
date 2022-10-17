#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Section 5.5.1 - Gaussian random numbers
Code for Q5.7
"""

from math import ceil
from numpy import arange, zeros, random
import matplotlib.pyplot as plt

# parameters
sample_size = 1000000
bin_width = 0.1
bin_min = -3.0  # all values lower than this go in the first bin [0]
bin_max = 3.0   # all values greater than this go in the last bin [bin_size -1]
 
# care must be taken to ensure that very few values fall outside bin_min to bin_max

# this time bin_size is twice the previous size to accommodate negative values
bin_size = int((bin_max - bin_min) / bin_width )
bin_range = arange(bin_min, bin_max, bin_width)

#print("bin_size=" + str(bin_size))
#print("bin_range=" + str(bin_range))


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
    return 0

#test_bin_index()
#test_bin_value()
    
gbin = zeros(bin_size, int) # gaussian random number

# to count values that lie outside the range -2 to +2
count_outside_range = 0
count_inside_range = 0

for value in random.normal(size = sample_size):
    idx = bin_index(value)
    gbin[idx] = gbin[idx] + 1
    if (value < -2.0) or (value > 2.0):
        count_outside_range += 1
    else:
        count_inside_range += 1
        
    # print("value=" + str(value) + " idx=" + str(idx)) # testing

prob_outside_range = count_outside_range / sample_size

# for testing:
#print("count outside range: " + str(count_outside_range))
#print("count inside range: " + str(count_inside_range))

print('Probability of value lying outside range -2 to +2 is ' + str(prob_outside_range))

"""
Q5.7
The probability that x lies outside the range -2 < x < 2
is calulated by counting the number of values that fall outside this
range during the binning process.
From that we can calulate what proportion this is of the whole sample.
Running the script several times shows this to be around 0.045.
"""

x = arange (0, bin_size) # range of bins
xt = [bin_value(idx) for idx in x] # to display random number values on x-axis

# reduce number of xticks displayed
c = 0
for i in xt:
    # only keep ticks that are divisible by a half
    d = xt[c] / 0.5
    if (d.is_integer() == False):
        xt[c] = ''
    c = c + 1

font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 22}

plt.clf()
plt.rc('font', **font)

plt.plot(x, gbin)
plt.xticks(x, xt)
plt.title('Gaussian random numbers')
plt.xlabel('Bins')
plt.ylabel('Count')

#plt.show()
plt.savefig("gaussian_random_numbers.png")



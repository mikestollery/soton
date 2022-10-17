#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Section 5.4 - Averages of random numbers
Code for Q5.5
"""

from numpy import arange, zeros, random
import matplotlib.pyplot as plt

# parameters
sample_size = 100000
bin_width = 0.05

bin_size = int(1 / bin_width)   # bin_size is number of bins used
"""
Note: bin_size * bin_width must equal 1.0 because the range of
random values is:
    0.0 <= value < 1.0
and so the total width of all the bins must be 1.0
e.g. bin_width of 0.05 gives 20 bins
"""

def bin_index(value):
    """
    Returns the index of the bin that this value should be put in
    Assumes value is in the range 0.0 to 0.999999...
    """
    d = value * bin_size
    return int(d)
    
def test_bin_index(increment = 0.01):
    """
    For testing bin_index
    This allows us to see that values go into their correct bins
    """
    vlist = arange (0, 1.0, increment)
    for v in vlist:
        ind = bin_index(v)
        print (str("{:.2f}".format(v)) + ' ==> ' + str(ind))
 
#test_bin_index()
    
bin1 = zeros(bin_size, int) # single random number
bin2 = zeros(bin_size, int) # average of 2 random numbers
bin3 = zeros(bin_size, int) # average of 3 random numbers
bin4 = zeros(bin_size, int) # average of 4 random numbers

for i in range (sample_size):
    y1 = random.random()
    y2 = (random.random() + random.random())/2
    y3 = (random.random() + random.random() + random.random())/3
    y4 = (random.random() + random.random() + random.random() + random.random())/4

    ind1 = bin_index(y1)
    ind2 = bin_index(y2)
    ind3 = bin_index(y3)
    ind4 = bin_index(y4)
    bin1[ind1] = bin1[ind1] + 1
    bin2[ind2] = bin2[ind2] + 1
    bin3[ind3] = bin3[ind3] + 1
    bin4[ind4] = bin4[ind4] + 1

x = arange (0, bin_size) # range of bins
xt = [i / bin_size for i in x] # to display random number values on x-axis

#print(x)
#print (xt)
#print (bin1)
#print (bin2)
#print (bin3)
#print (bin4)

font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 22}

plt.clf()
plt.rc('font', **font)

plt.subplot(4, 1, 1)
plt.plot(x, bin1)
plt.xticks(x, xt)
plt.title('Single random numbers')
plt.xlabel('Bins')
plt.ylabel('Count')
plt.ylim(0, max(bin1) * 2) # for better view of distribution

plt.subplot(4, 1, 2)
plt.plot(x, bin2)
plt.xticks(x, xt)
plt.title('Average of 2 random numbers')
plt.xlabel('Bins')
plt.ylabel('Count')


plt.subplot(4, 1, 3)
plt.plot(x, bin3)
plt.xticks(x, xt)
plt.title('Average of 3 random numbers')
plt.xlabel('Bins')
plt.ylabel('Count')

plt.subplot(4, 1, 4)
plt.plot(x, bin4)
plt.xticks(x, xt)
plt.title('Average of 4 random numbers')
plt.xlabel('Bins')
plt.ylabel('Count')


plt.subplots_adjust( hspace = 0.5)

#plt.show()
plt.savefig("distributions_of_random_numbers.png")

"""
Q5.6
Averages of random numbers cause a bell curve peaking at the centre,
in contrast to the roughly straight even spread of single random numbers.
This is because in a group of random numbers to be averaged,
The probabilty of them all being either at the low end of the range or
the top end of the range is less than the probability of them having 
an even spread.
Similarly, rolling two dice will give a better chance of scoring 7 than
2 or 12.
"""


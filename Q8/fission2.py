# -*- coding: utf-8 -*-

"""
Q8.2 Using neutrons function
"""

from numpy import random
from math import sqrt
from neutrons import neutrons

L = 20 # length of line of uranium (cm)
a = 1.7 # mean free path for bounce (cm)
b = 21  # mean free path for fission (cm)

initial_fissions = 100
secondary_fissions = 0

R = sqrt(2 * a * b)
print ('L=' + str(L) + ' a=' + str(a) + ' b=' + str(b) + ' R=' + str(round(R, 3)))

for i in range (0, initial_fissions):
    pos1 = L * random.random()  # position of initial fission
    
    # number of neutrons produced by initial fission
    for n in range(0, neutrons()):   
        if (random.random() < 0.5):
            dir = -1    # neutron moves to the left
        else:
            dir = 1 # neutron moves to the right
            
        # position of secondary fission
        pos2 = pos1 + (dir * R)
        if pos2 >= 0 and pos2 <= L:
            # neutron remains within uranium bar
            secondary_fissions += 1
            
        print('i=' + str(i) + ' n=' + str(n) + ' pos1=' + str(round(pos1, 2)) \
             + ' dir=' + str(dir) + ' pos2=' + str(round(pos2, 2)))
        
print ('L=' + str(L) + 'cm initial_fissions=' + str(initial_fissions) + \
    ' secondary_fissions=' + str(secondary_fissions))
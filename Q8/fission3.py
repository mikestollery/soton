# -*- coding: utf-8 -*-

"""
Q8.3 Varying L to find its critical value
"""

from numpy import random
from math import sqrt
from neutrons import neutrons
    
a = 1.7 # mean free path for bounce (cm)
b = 21  # mean free path for fission (cm)

initial_fissions = 1000

R = sqrt(2 * a * b)

def calc_secondary_fissions(initial_fissions, L):
    secondary_fissions = 0
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
    return secondary_fissions

critical_length = 0
for L in range(10, 20):
    secondary_fissions = calc_secondary_fissions(initial_fissions, L)
    result = ''
    if secondary_fissions > initial_fissions:
        result = 'Boom!'
        if critical_length <= 0:
            critical_length = L
    print ('L=' + str(round(L/100, 2)) + 'm initial_fissions=' + str(initial_fissions) + ' secondary_fissions=' + str(secondary_fissions) + ' ' + result)
  
print ('critical_length=' + str(round(critical_length/100, 2)) + ' metres')
       
"""
With 100 initial fissions, uranium usually explodes at 0.15m
but sometimes does at 0.14m and even at 0.13m.

Increasing to 1000 initial fissions makes the result more consistently at 0.15m
"""
# -*- coding: utf-8 -*-

"""
Q8.4 Updated for 3-dimensional model
"""

from numpy import random
from math import sqrt, pi, sin, cos, acos
from neutrons import neutrons, diffusion
    
a = 1.7 # mean free path for bounce (cm)
b = 21  # mean free path for fission (cm)

initial_fissions = 100

R = sqrt(2 * a * b)

def calc_secondary_fissions(initial_fissions, L):
    secondary_fissions = 0
    for i in range (0, initial_fissions):
        # position of initial fission (x1, y1, z1)
        x1 = L * random.random()  
        y1 = L * random.random()  
        z1 = L * random.random()  
    
        # number of neutrons produced by initial fission
        for n in range(0, neutrons()):  
            # calculate position of secondary fission (x2, y2, z2)
            phi = 2.0*pi*random.random()
            theta = acos(2.0*random.random() - 1.0)
            s = diffusion() * R
            x2 = x1 + s*sin(theta)*cos(phi)
            y2 = y1 + s*sin(theta)*sin(phi)
            z2 = z1 + s*cos(theta)
            
            # distance travelled (for testing - d should always equal s)
            d = sqrt(abs(x2 - x1)**2 + abs(y2 - y1)**2 + abs(z2 - z1)**2)
            
            print('i=' + str(i) + ' s=' + str(round(s, 2)) + ' (x1, y1, z1)=(' \
                + str(round(x1, 2)) + ', ' + str(round(y1, 2)) + ', ' \
                + str(round(z1, 2)) + ') ==> (x2, y2, z2)=(' \
                + str(round(x2, 2)) + ', ' + str(round(y2, 2)) + ', ' \
                + str(round(z2, 2)) + ') d=' + str(round(d, 2))) 
            
            if x2 >= 0 and x2 <= L \
                and y2 >= 0 and y2 <= L \
                and z2 >= 0 and z2 <= L:                    
                # neutron remains within uranium cube
                secondary_fissions += 1

    return secondary_fissions

L = 20  # cm
secondary_fissions = calc_secondary_fissions(initial_fissions, L)
print ('L=' + str(L) + ' initial_fissions=' + str(initial_fissions) \
       + ' secondary_fissions=' + str(secondary_fissions))



       

# -*- coding: utf-8 -*-

"""
Q8.5 Vary L to find critical mass
"""

import time
from numpy import random, arange
from math import sqrt, pi, sin, cos, acos
from neutrons import neutrons, diffusion
    
a = 1.7 # mean free path for bounce (cm)
b = 21  # mean free path for fission (cm)

initial_fissions = 10000

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
            
            if x2 >= 0 and x2 <= L \
                and y2 >= 0 and y2 <= L \
                and z2 >= 0 and z2 <= L:                    
                # neutron remains within uranium cube
                secondary_fissions += 1

    return secondary_fissions

t0 = time.time()
critical_length = 0

# selected a finer granularity for L to obtain a more precise result.
for L in arange(14, 16, 0.01):
    secondary_fissions = calc_secondary_fissions(initial_fissions, L)
    result = ''
    if secondary_fissions > initial_fissions:
        result = 'Boom!'
        
        # For efficiency we could break the loop here
        # but let's continue and report all results
        if critical_length <= 0:
            critical_length = L
    print ('L=' + str(round(L/100, 4)) + 'm initial_fissions=' + str(initial_fissions) \
           + ' secondary_fissions=' + str(secondary_fissions) + ' ' + result)

critical_length /= 100   # convert cm to metres
critical_volume = critical_length**3
critical_mass = 18700 * critical_volume
t1 = time.time() - t0
    
print ('critical_length=' + str(round(critical_length, 2)) + 'm')
print ('critical_volume=' + str(round(critical_volume, 6)) + 'm^3')
print ('critical_mass=' + str(round(critical_mass, 2)) + 'kg')
print ('Time taken: ' + str(round(t1, 1)) + ' seconds')

"""
Program shows critical mass to be approx 60 kg

Actual critical mass of a U-235 sphere is 50 kg
but this is a cube and so would require a greater volume.
"""

# -*- coding: utf-8 -*-
"""
Q6.6 Use g(t) = cos(t)
"""

import matplotlib.pyplot as plt
from math import cos

w = 1.0

def g(t):
    return cos(w * t)

def f(y, t):
    return -y + g(t)

def odestep(f, y, t, dt):
    slope_at_a = f(y, t)
    y_at_b = y + slope_at_a * dt
    slope_at_b = f(y_at_b, t)
    avg_slope = (slope_at_a + slope_at_b) / 2
    return y + dt*avg_slope

t = 0; y = 0.0; dt = 0.1
tf = 20.0
nsteps = int(tf/dt)
print (t, y)

# array of values starting at initial value
tvalues = [t]
yvalues = [y]
gvalues = [g(t)]

for i in range( nsteps ):
    gval = g(t)
    y = odestep(f, y, t, dt)
    t = (i + 1) * dt
    #print (t, y)
    tvalues.append(t)
    yvalues.append(y)
    gvalues.append(gval)
    
print(tvalues)
print(yvalues)
print(gvalues)

#plt.subplot(1, 1, 1)
plt.plot(tvalues, gvalues)
plt.title('Input voltage g')
plt.xlabel('t')
plt.ylabel('g')
#plt.subplot(1, 1, 1)
plt.plot(tvalues, yvalues)
plt.title('Output voltage y')
plt.xlabel('t')
plt.ylabel('y')

#plt.subplots_adjust( hspace = 0.5)
plt.savefig("q6work3.png")

# -*- coding: utf-8 -*-
"""
6.2 An improved algorithm
"""

def g(y, t):    # input voltage
    return 1.0

def f(y, t):    # gradient at t
    return -y + g(y, t)

def odestep(f, y, t, dt):
    slope_at_a = f(y, t)
    #y_at_b = y + slope_at_a * (t+dt)
    y_at_b = y + slope_at_a * dt
    slope_at_b = f(y_at_b, t)
    avg_slope = (slope_at_a + slope_at_b) / 2
    print("t=" + str(round(t, 1)) + " slope at a=" + str(slope_at_a) + " b=" + str(slope_at_b) + " avg=" + str(avg_slope))
    return y + dt*avg_slope

t = 0; y = 0; dt = 0.1
tf = 15.0; nsteps = int(tf/dt)
print (t, y)

tvalues = [t]
yvalues = [y]

for i in range( nsteps ):
    y = odestep(f, y, t, dt)
    t = (i + 1) * dt
    #print (t, y)

    tvalues.append(t)
    yvalues.append(y)
    
#print(tvalues)
#print(yvalues)

import matplotlib.pyplot as plt
plt.plot(tvalues, yvalues)
plt.title('Plot for g(y, t) = 1')
plt.xlabel('t')
plt.ylabel('y')
plt.show()
plt.savefig("q6work2.png")
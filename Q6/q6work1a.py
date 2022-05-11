# -*- coding: utf-8 -*-
"""
6.1 The computer solution
"""

def f(y, t):
    return -y + 1.0

def odestep(f, y, t, dt):
    slope_at_a = f(y, t)
    y_at_b = y + slope_at_a * (t+dt)
    slope_at_b = f(y_at_b, t)
    avg_slope = (slope_at_a + slope_at_b) / 2
    #print ("     slope_at_a=" + str(slope_at_a) + " y_at_b=" + str(round(y_at_b, 4)))
    #print ("     slope_at_b=" + str(slope_at_b) + " avg_slope=" + str(round(avg_slope, 4)))
    #return y + dt*f(y, t)
    return y + dt*avg_slope

t = 0; y = 0; dt = 0.2
tf = 2.0; nsteps = int(tf/dt)
print (t, y)

print("nsteps=" + str(nsteps) + " dt=" + str(dt))

for i in range( nsteps ):
    #print("i=" + str(i))
    f1 = f(y, t)
    #print("  y=" + str(y) + " t=" + str(round(t, 2)) + " f1=" + str(round(f1, 4)))
    y = odestep(f, y, t, dt)
#    print("  y=" + str(y))
    t = (i + 1) * dt
    f2 = f(y, t)
    print("  y=" + str(y) + " t=" + str(round(t, 2)) + " f2=" + str(round(f2, 4)))

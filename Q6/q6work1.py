# -*- coding: utf-8 -*-
"""
6.1 The computer solution
"""

def f(y, t):
    return -y + 1.0

def odestep(f, y, t, dt):
    return y + dt*f(y, t)

t = 0; y = 0; dt = 0.01
tf = 2.0; nsteps = int(tf/dt)
print (t, y)

for i in range( nsteps ):
    y = odestep(f, y, t, dt)
    t = (i + 1) * dt
    print (t, y)

"""
For dt = 0.2
t = 1.0 ==> y = 0.67232
t = 2.0 ==> y = 0.8926258176

For dt = 0.1
t = 1.0 ==> y = 0.65132156
t = 2.0 ==> y = 0.8784233454094308

For dt = 0.02
t = 1 ==> y = 0.6358303199128829
t = 2 ==> y = 0.867380444105247

For dt = 0.01
t = 1 ==> y = 0.6339676587267709
t = 2 ==> y = 0.8660203251420382

"""
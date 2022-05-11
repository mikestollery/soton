# -*- coding: utf-8 -*-
"""
Q6.6 Use g(t) = cos(t)
"""

import matplotlib.pyplot as plt
from math import cos



def g(w, t):
    return cos(w * t)

def f(y, w, t):
    return -y + g(w, t)

def odestep(f, y, w, t, dt):
    slope_at_a = f(y, w, t)
    y_at_b = y + slope_at_a * dt
    slope_at_b = f(y_at_b, w, t)
    avg_slope = (slope_at_a + slope_at_b) / 2
    return y + dt*avg_slope

def plotgraph(w, subplot):
    t = 0; y = 0.0; dt = 0.1
    tf = 20.0
    nsteps = int(tf/dt)
    print (t, y)
    print('nsteps=' + str(nsteps))

    # array of values starting at initial value
    tvalues = [t]
    yvalues = [y]
    gvalues = [g(w, t)]

    for i in range( nsteps ):
        gval = g(w, t)
        y = odestep(f, y, w, t, dt)
        t = (i + 1) * dt
        #print (t, y)
        tvalues.append(t)
        yvalues.append(y)
        gvalues.append(gval)
    
    print(tvalues)
    print(yvalues)
    print(gvalues)

    plt.subplot(3, 1, subplot)
    plt.plot(tvalues, gvalues)
    plt.title('Omega = ' + str(w))
    plt.plot(tvalues, yvalues)
    plt.xlabel('t')
    plt.ylabel('voltage')


plotgraph(0.5, 1)
plotgraph(1.0, 2)
plotgraph(2.0, 3)

#plt.rcParams["figure.figsize"] = (8,8)
plt.subplots_adjust( hspace = 2.0)
plt.savefig("q6work3.png")
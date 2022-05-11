# -*- coding: utf-8 -*-

from math import fabs, e

# 4.1 The trapezium rule

# Q4.1
def integrand (x):
    # integrand of 4.1
    return (x**4 * (1 - x)**4) / (1 + x**2)


def trap0 (f, a, b, n):
    """ Basic trapezium rule. Integrate f(x) over the
    interval from a to b using n strips . """
    h = float(b - a)/n
    s = 0.5*(f(a) + f(b))
    for i in range (1, n):
        s = s + f(a + i*h)
    return s*h

"""
n is number of trapeziums used in test script.
At 100 trapeziums the value changes in the 9th sig fig
At 1000 trapeziums the value changes only in the 15th sig fig
At 10000 trapeziums the value stops changing.
"""
n = 1000

area = trap0(integrand, 0, 1, n)
print ("trapeziums=" + str(n) + " area=" + str(area))

"""
trapeziums=100   area=0.0012644892673714441
trapeziums=1000  area=0.0012644892673496183
trapeziums=10000 area=0.0012644892673496183

Q4.2
value of integral is 0.0012644892673496183

The graph plotted in q4plot1.py shows that this
looks like a reasonable result.
"""

def test_trap0():
    for n in range (1, 20):
        area = trap0(integrand, 0, 1, n)
        print ("n=" + str(n) + " area=" + str(area))
        
        
test_trap0()

"""
Integral stops changing by 6 sig fig at n=12
n=10 area=0.0012645110928411146
n=11 area=0.0012645015872536428
n=12 area=0.0012644965766461479
n=13 area=0.0012644937890595059

Q4.3 12 trapeziums are needed.
"""

# 4.2 Getting a specified accuracy

def trap1(f, a, b, delta, maxtraps = 512):
    """ 
    Improved trapezium rule. Integrate f(x) over
    interval from a to b, trying to get relative accuracy
    delta . Optional last argument is maximum allowed
    number of trapezia. 
    """
    n = 8
    inew = trap0 (f, a, b, n)
    iold = -inew # make sure we do not terminate immediately
    while (fabs(inew - iold) > delta * fabs(inew)):
        iold = inew
        n = 2 * n
        if n > maxtraps:
            print (" Cannot reach requested accuracy with", \
                   maxtraps, " trapezia")
            return
        inew = trap0(f, a, b, n)
    return inew

delta = 1.0e-13
trap1_area = trap1(integrand, 0, 1, delta)

print ("4.2: delta=" + str(delta) + " trap1_area=" + str(trap1_area))

"""
If delta is smaller than 1.0e-13 you need to increase maxtraps, e.g.
trap1_area = trap1(integrand, 0, 1, delta, 1024)

"""

# 4.3 Code development

# 4.4 Another integral

def e_integrand(x):
    return e**(-x**2)

"""
a = -infinity, b = +infinity
Need to choose finite values
"""

a = -10
b = +10
e_delta = 1.0e-4

e_int = trap1(e_integrand, a, b, e_delta)

print("a=" + str(a) + " b=" + str(b) + " e_delta=" + str(e_delta) + " e_int=" + str(e_int))

"""
a=-10 b=10 e_delta=0.0001 e_int=1.7724538509055157

The graph plotted in q4plot1.py shows that this
looks like a reasonable result.
"""






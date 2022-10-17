# -*- coding: utf-8 -*-

while True:
    n = int( input(" Enter number of trapeziums: " ))
    h = 1.0 / n
    intgrl = 0.0
    for i in range (1, n):
            intgrl = intgrl + h*(i*h)**4 * (1 - i*h)**4/(1 + i*h*i*h)
            print(n, intgrl )
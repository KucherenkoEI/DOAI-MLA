import numpy as np
from numpy.ma.core import arange

x1 = 2
xn = 8
dx = 0.7
a = 4.2
b = 1.5

def fx(x):
    return (1+a*x+b*np.cos(x)**(1/2))

print('цикл while')
while not x1 >= xn:
    x1 += dx
    print('x= ', round(x1, 3), 'f(x) = ', round(fx(x1), 7))

print('цикл for')
for i in np.arange(x1, xn, dx):
    print('x= ', round(i, 3), 'f(x) = ', round(fx(i), 7))
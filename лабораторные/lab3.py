import numpy as np
x1 = 2
xn = 8
dx = 0.7
a = 4.2
b = 1.5


def fx(x):
    return ((1+a*x+b*np.cos(x))**(1/2))


n = x1
print('цикл while')
while not n >= xn:
    n += dx
    print('x= ', round(n, 3), 'f(x) = ', round(fx(n), 7))
print('цикл for')
for i in np.arange(x1, xn, dx):
    print('x= ', round(i, 3), 'f(x) = ', round(fx(i), 7))

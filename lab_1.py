from numpy import *

x, y, z = int(input('x=')), int(input('y=')), int(input('z='))
a = 5 * arctan(x)
b = 1 / 4 * arccos(x)
c = (abs(x - y) + x * x) / (abs(x - y) * z)
s = a - b * c
print('s=', s)

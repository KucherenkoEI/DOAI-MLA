import math as m
import sys

x = float(input("Введите значение x -> "))
y = float(input("Введите значение y -> "))
i = None

fvid = float(input("fx=: 1 если tgh(y), 2 если 2**у, 3 если sh(x/y), 4 если 0"))
match fvid:
    case 1:
        fx = m.tanh(y)
    case 2:
        fx = 2**y
    case 3:
        fx = m.sinh(x/y)
    case 4:
        fx = 0
    case _:
        print("Неверный выбор")
        sys.exit()

if ( x * y ) > 1 and (x * y) < 10:
    i = m.exp(fx)
elif (x*y) > 0.1 and (x*y) < 0.5:
    i = (m.fabs(fx+4*y))**(1/3)
else: i = (fx**2) * y

print ("c=", i)
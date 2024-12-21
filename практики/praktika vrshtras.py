import numpy as np
import matplotlib.pyplot as plt

def vrshtras(x, a, b, skolko):
    otvet = 0
    for n in range(skolko):
        otvet += a ** n * np.cos(b ** n * np.pi * x)
    return otvet
#где otvet-это выдаваемое функцией значение.
#return нужен потому, что потом присвоим другой переменной значение otvet

print('тестировалось при: а=0.5, b=3, 100 значениях, диапазоне[-2;2] на 100000')
a = float(input('введите а '))
b = float(input('введите b '))
slolko= int(input('сколько значений? '))
ot= int(input('x: диапазон от '))
do= int(input('х: диапазон до '))
chislo= int(input('х: сколько значений в диапазоне? '))

diapason_x = np.linspace(start = ot, stop = do, num = chislo)
diapason_y = vrshtras(diapason_x, a, b, slolko)

fig, ax = plt.subplots(figsize=(10, 10))
ax.plot(diapason_x, diapason_y, label='функция Виерштрасса')
ax.grid(True)
plt.show()

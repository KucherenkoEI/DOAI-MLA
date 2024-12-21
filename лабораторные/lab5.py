x = int(input('сколько элементов? '))
spisok = []
r=0
s=1

for i in range(x):
    spisok.append(int(input('Ввведите элемент списка')))

p = max(spisok)
v = spisok.index(min(spisok))
spisok[spisok.index(max(spisok))] = min(spisok)
spisok[v] = p
print('с перестановкой переменных',spisok)

for i in range(len(spisok)):
    if spisok[i] % 2 == 0:
        r = r + spisok[i]
    else:
        s = s* spisok[i]

print('сумма чётных ', r)
print('произведение нечётных', s)

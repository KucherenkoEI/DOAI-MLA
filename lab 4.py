str = input("Введите строку -> ")

str = str.replace('.', '').replace(',','').replace('!','')
print(str)

slova = str.split()
print(len(slova))
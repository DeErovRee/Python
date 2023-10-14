from random import randint

n = int(input('Введите число монет: '))
a, b = 0, 0
for i in range(n): 
    moneta = randint(0,1)
    print(moneta, end=" ")
    if moneta > 0:
        a += 1
    else: b += 1
print()
if a > b: 
    print(f'Нужно перевернуть монеток: {b}')
else: print(f'Нужно перевернуть монеток: {a}')
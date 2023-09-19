n = int(input('Введите число N: '))

k, res = 0, 1
while res < (n+1):
    print(res, end=" ")
    k += 1
    res = 2 ** k
print()
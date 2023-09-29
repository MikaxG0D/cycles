x = int(input('Введите число: '))

fac = 1

for i in range(1, x + 1):
    fac *= i
print(fac)
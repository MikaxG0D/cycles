x = int(input("Введите число: "))
y = int(input('Введите степень: '))

xiny = 1

for i in range(y):
    xiny *= x
print(xiny)
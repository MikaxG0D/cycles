x = int(input('Введите число: '))

total = 0
mult = 1

while x > 0:
    total += x % 10
    mult *= x % 10
    x = x // 10
print(f'Сумма - {total}')
print(f'Произведение - {mult}')
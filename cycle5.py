N = int(input('Введите число: '))

num = 1
prevnum = 1

for _ in range(N):
    print(num)
    num, prevnum = num + prevnum, num

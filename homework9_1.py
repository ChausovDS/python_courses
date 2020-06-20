maxsumm = 0
number = 0
while True:
    x = int(input('введите число или 0 для завершения программы '))
    if x == 0:
        break
    summ = 0
    x_to_save = x
    while x > 0:
        summ += x % 10
        x //= 10
    if summ > maxsumm:
        maxsumm = summ
        number = x_to_save
print(f'{maxsumm}, {number}')
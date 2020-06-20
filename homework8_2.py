def many_number(c, n, counter=0):
    if c == 0:
        return counter
    x = int(input('введите число: '))
    while x > 0:
        if x % 10 == n:
            counter += 1
        x //= 10
    return many_number(c-1, n, counter)


count = int(input('сколько будет чисел? '))
number = int(input('какую цифру ищем? '))
print(f'в введенных числах {many_number(count, number)} чисел {number}')

count = int(input('сколько будет чисел? '))
number = int(input('какую цифру ищем? '))
counter = 0
for i in range(count):
    x = int(input(f'введите {i+1} число '))
    while x > 0:
        if x % 10 == number:
            counter += 1
        x //= 10

print(f'было введено {counter} цифр "{number}"')

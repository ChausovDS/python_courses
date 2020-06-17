while True:
    x = input('введите знак операции (+, -, /, *, либо 0 для выхода: ')
    if x == '0':
        break
    elif x == '+':
        first_n = int(input('введите первое слагаемое'))
        second_n = int(input('введите второе слагаемое'))
        print(f'{first_n} + {second_n} = {first_n + second_n}')
    elif x == '-':
        first_n = int(input('введите уменьшаемое'))
        second_n = int(input('введите вычитаемое'))
        print(f'{first_n} - {second_n} = {first_n - second_n}')
    elif x == '*':
        first_n = int(input('введите первый множитель'))
        second_n = int(input('введите второй множитель'))
        print(f'{first_n} * {second_n} = {first_n * second_n}')
    elif x == '/':
        first_n = int(input('введите делимое'))
        second_n = int(input('введите делитель'))
        try:
            print(f'{first_n} / {second_n} = {first_n / second_n}')
        except ZeroDivisionError:
            print('делить на ноль запрещено')
    else:
        print("введите один из предложенных выше символов")

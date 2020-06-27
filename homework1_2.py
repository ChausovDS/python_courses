def calc(result):
    print(result)
    sign = input('введите знак операции (+, -, /, *, либо 0 для выхода): ')
    if sign == '0':
        return 0
    elif sign == '+':
        first_n = int(input('введите первое слагаемое '))
        second_n = int(input('введите второе слагаемое '))
        return calc(first_n + second_n)
    elif sign == '-':
        first_n = int(input('введите уменьшаемое '))
        second_n = int(input('введите вычитаемое '))
        return calc(first_n - second_n)
    elif sign == '*':
        first_n = int(input('введите первый множитель'))
        second_n = int(input('введите второй множитель'))
        return calc(first_n * second_n)
    elif sign == '/':
        first_n = int(input('введите делимое'))
        second_n = int(input('введите делитель'))
        try:
            first_n / second_n
        except ZeroDivisionError:
            calc('деление на 0 запрещено')
    else:
        return calc('введите один из предложенных сверху символов')


calc('')

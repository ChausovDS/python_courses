def add_numeral(number, maximum = 0):
    if number == 0:
        return maximum
    summ = 0
    numb_to_count = number
    while numb_to_count > 0:
        summ += numb_to_count % 10
        numb_to_count //= 10
    if summ > maximum:
        maximum = summ
    return add_numeral(int(input('введите число или 0 для выхода ')), maximum)


print(add_numeral(int(input('введите число или 0 для выхода '))))

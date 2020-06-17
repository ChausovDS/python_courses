from sys import exit


def reverse_number(number, new_number=''):
    if number == 0:
        return new_number
    new_number += str(number % 10)
    return reverse_number(number // 10, new_number)


try:
    NUMBER = int(input('введите натуральное число '))
except ValueError:
    print('было введено не число')
    exit()
print(reverse_number(NUMBER))

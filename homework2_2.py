from sys import exit


def count_even_digits(number, even=0, not_even=0):
    if number == 0:
        return f'в числе {even} четных и {not_even} нечетных цифр'
    if number % 2 == 0:
        even += 1
        return count_even_digits(number // 10, even, not_even)
    else:
        not_even += 1
        return count_even_digits(number // 10, even, not_even)


try:
    number = int(input('введите натуральное число'))
except ValueError:
    print('было введено не число')
    exit()

print(count_even_digits(number))

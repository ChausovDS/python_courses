from sys import exit
try:
    number = int(input('введите натуральное число'))
except ValueError:
    print('было введено не число')
    exit()
even = 0
not_even = 0
number1 = number
while True:
    if number1 == 0:
        break
    if number1 % 2 == 0:
        even += 1
    else:
        not_even += 1
    number1 //= 10

print(f'в числе {number} {even + not_even} цифр, из которых {even} четных и {not_even} нечетных цифр')

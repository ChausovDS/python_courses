from sys import exit
try:
    number = int(input('введите натуральное число'))
except ValueError:
    print('было введено не число')
    exit()
new_number = ''
while True:
    if number == 0:
        break
    adding = str(number % 10)
    new_number += adding
    number //= 10

print(f'перевернутое число: {new_number}')

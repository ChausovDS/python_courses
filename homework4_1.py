from sys import exit
try:
    n = int(input('введите натуральное число'))
except ValueError:
    print('было введено не число')
    exit()
summ = 0
for i in range(n):
    if i % 2 == 0:
        summ += (1 / 2 ** i)
    else:
        summ -= (1 / 2 ** i)
print(summ)


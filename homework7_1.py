from sys import exit

try:
    n = int(input('введите натуральное число '))
except ValueError:
    print('было введено не число')
    exit()
summ = 0
for i in range(1, n + 1):
    summ += i
print(
    f' сумма чисел от 1 до {n} равна {summ}, результат формулы n(n+1)/2 равен {n*(n+1)//2}')
if summ == n * (n + 1) // 2:
    print('проверка успешна')
else:
    print('проверка неудачна')

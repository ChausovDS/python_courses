from sys import exit


def summ(n):
    if n == 1:
        return n
    return n + summ(n - 1)


try:
    n = int(input('введите натуральное число '))
except ValueError:
    print('было введено не число')
    exit()

print(
    f' сумма чисел от 1 до {n} равна {summ(n)}, результат формулы n(n+1)/2 равен {n*(n+1)//2}')
if summ(n) == n * (n + 1) // 2:
    print('проверка успешна')
else:
    print('проверка неудачна')

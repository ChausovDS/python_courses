def sum_between(array):
    a = array.index(min(array))
    b = array.index(max(array))
    check = abs(a-b) - 1
    start = min([a, b]) + 1
    if check > 0:
        return sum(array[start:start+check])
    else:
        return 0


n = int(input('введите количество элементов в массиве '))
lst = []
for i in range(n):
    lst.append(int(input('введите число')))

print(f'введен массив {lst}')
print(f'сумма элементов между минимальным {min(lst)} и максимальным {max(lst)} равно {sum_between(lst)}')

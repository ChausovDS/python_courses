def double_min(array):
    min1 = min(array)
    array.remove(min1)
    min2 = min(array)
    print(f'первый минимальный элемент {min1}')
    if min1 != min2:
        print(f'второй {min2}')
    else:
        print('он встречается два раза')


lst = [28, -86, 44, -37, -7, -52, -19, -3, -15, -73, -86]
print(f'исходный массив {lst}')
double_min(lst)

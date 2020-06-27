def big_from_small(array):
    lst_of_min = []
    for i in array:
        lst_of_min.append(min(i))
    return lst_of_min, max(lst_of_min)


strings = int(input('введите количество строк '))
not_strings = int(input('введите количество столбцов '))
matrix = []
for i in range(strings):
    matrix.append([])
    for j in range(not_strings):
        matrix[i].append(
            int(input(f'введите число для {i + 1} строки, {j + 1} элемента ')))

result = big_from_small(matrix)
print(f'минимальные значения по столбцам: {result[0]}')
print(f'максимальное из минимальных: {result[1]}')

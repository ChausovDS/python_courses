matrix = []
for i in range(5):
    matrix.append([])
    for j in range(4):
        matrix[i].append(
            int(input(f'введите число для {i+1} строки, {j+1} элемента ')))

    matrix[i].append(sum(matrix[i]))

for i in range(5):
    print(f'{i+1}-я строка: ')
    for j in range(4):
        print(matrix[i][j])


for i in matrix:
    print(i)

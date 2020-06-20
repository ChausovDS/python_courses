from random import randint


def change_pos(array):
    mn = array.index(min(array))
    mx = array.index(max(array))
    array[mn], array[mx] = array[mx], array[mn]


lst = [randint(0, 100) for i in range(10)]
print(lst)
change_pos(lst)
print(lst)

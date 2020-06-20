def max_und_zero(array):
    near_zero = 0
    for i in array:
        if i < 0 and (i > near_zero or near_zero == 0):
            near_zero = i
    return near_zero, array.index(near_zero)


array = [-55, -69, -5, 72, -41, -58, -79, 58, 74, 1]
print(max_und_zero(array))

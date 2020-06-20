def quotient(mn, mx):
    lst_of_div = [0 for i in range(0, 10)]
    for i in range(mn, mx+1):
        for j in range(2, 10):
            if i % j == 0:
                lst_of_div[j] += 1
    return lst_of_div


lst = quotient(2, 99)
for i in range(2, 10):
    print(f'в диапазоне 2-99: {lst[i]} чисел делятся на {i}')
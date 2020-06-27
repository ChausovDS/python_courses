from collections import defaultdict


def calc():
    num_to_calc = defaultdict(list)
    for i in range(2):
        n = input(f'введите {i+1}-е 16-ричное число')
        num_to_calc[f'{i+1} - {n}'] = list(n)
    print(num_to_calc)

    summ = sum([int(''.join(i), 16) for i in num_to_calc.values()])
    print('Cумма: ', list('%X' % summ))


calc()

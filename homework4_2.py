from sys import exit


def sequence(count, summ=0):
    count -= 1
    if count == 0:
        return summ + 1
    if count % 2 == 0:
        summ += (1 / 2 ** count)
        return sequence(count, summ)
    else:
        summ -= (1 / 2 ** count)
        return sequence(count, summ)


try:
    n = int(input('введите натуральное число'))
except ValueError:
    print('было введено не число')
    exit()
print(sequence(n))

from random import randint


def guess_game(user_try, answer, lifes):
    if lifes == 0:
        return f'вы проиграли, загаданное число {answer}'
    if user_try == answer:
        return 'вы угадали'
    else:
        if user_try > answer:
            print(f'загаданное число меньше, попробуйте еще раз. осталось {lifes-1} попыток')
        else:
            print(f'загаданное число больше, попробуйте еще раз. осталось {lifes-1} попыток')
        return guess_game(int(input('введите число от 0 до 100 ')), answer, lifes - 1)


print(guess_game(int(input('введите число от 0 до 100 ')), randint(0, 100), 10))

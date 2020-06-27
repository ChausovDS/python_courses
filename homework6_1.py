from random import randint
answer = randint(0, 100)
lifes = 10
while True:
    try:
        user_try = int(input('угадайте число от 0 до 100 '))
    except ValueError:
        print('необходимо ввести число')
        continue
    if user_try == answer:
        print('вы угадали')
        break
    else:
        lifes -= 1
        if lifes == 0:
            print(f'вы проиграли, загаданное число {answer}')
            break
        if user_try > answer:
            print(f'загаданное число меньше, попробуйте еще раз. осталось {lifes} попыток')
        if user_try < answer:
            print(f'загаданное число больше, попробуйте еще раз. осталось {lifes} попыток')

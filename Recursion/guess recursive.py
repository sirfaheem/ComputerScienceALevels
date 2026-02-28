import random


def guess(n: int):
    try:
        inp = int(input('Enter a number between 1 and 10: '))
    except ValueError:
        print('Invalid input')
        guess(n)
        return #unreachable
    if (n == inp):
        print('Congratulation! You guessed it correctly.')
        return
    elif (n > inp):
        print('Enter a bigger number')
        guess(n)
    else:
        print('Enter a lesser number')
        guess(n)


guess(random.randint(1, 11))

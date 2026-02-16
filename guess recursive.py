import random
def guess(n):
    inp=int(input('Enter a number between 1 and 10: '))
    if(n==inp):
        print('Congratulation! You guessed it correctly.')
        return
    elif(n>inp):
        print('Enter a bigger number')
        guess(n)
    else:
        print('Enter a lesser number')
        guess(n)
guess(random.randint(1,11))

import random
thisNum = random.randint(1,100)

print(thisNum)

tries = 0

guess = int(input("Enter your guess: "))

while guess!=thisNum:
    if guess>thisNum:
        print("your guess is too high.")
    else:
        print("your guess is too low.")
    tries+=1
    guess = int(input("Enter your guess: "))

print(f'you guessed in {tries} attempts.')

import  random 

print('Guess the number that\'s in  my mind')

guessNo = random.randint(1,100)

for x in range (1,7):
    print("Make a guess")
    uGuess = int(input())
    if uGuess==guessNo:
        print("You guessed it right")
    elif uGuess>guessNo:
        print ("Sorry too high guess")
    else:
         print("your guess is too low")


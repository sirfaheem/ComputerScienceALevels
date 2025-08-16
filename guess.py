import random
secretNumber= random.randint(1,1000)
number=0
count = 0
while number!= secretNumber:
    number=int(input("enter a guess number \n >"))
    count = count + 1
    if number==secretNumber :
        print("correct")
        
    elif number < secretNumber:
        print("incorrect, try a bigger number")
    else:
        print ("incorrect, try a smaller number")
print ("number of attempts =" , (count))

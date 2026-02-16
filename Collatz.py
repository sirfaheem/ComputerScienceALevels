


def collatz(num):
    if(num<=1):
        return 1
    elif (num % 2 ==0):
        print(num//2)
        return collatz(num//2)
    else:
        print(3*num+1)
        return collatz(3*num+1)

print('Enter a number to print Collatz series')

myNum = int(input())

try:
    print (collatz(myNum))
    
except ValueError:
    print('not an integer')    


    

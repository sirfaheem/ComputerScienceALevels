##student work

global i
i = 2
global prime
prime = True


def isPrime(n: int):
    global prime, i
    if n == 1: # base case 1
        prime = False
    elif n == 2 or n == 3: # base case 2
        prime = True
    elif n > 3:
        if n > i:
            if n%i == 0:
                prime = False
            else:
                i+=1
                isPrime(n)

isPrime(3)
print(prime)
isPrime(4)
print(prime)
isPrime(5)
print(prime)
isPrime(6)
print(prime)

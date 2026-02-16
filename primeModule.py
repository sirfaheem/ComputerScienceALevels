def IsPrime(n): #returns True if it is prime
    
    i = 3
    found = False
    
    while i <= n and found == False:
        if n%i == 0:
            found = True
        else:
            i += 2
    if n==2: found = True
    return found

print(IsPrime(1),"1")
print(IsPrime(2),"2")
print(IsPrime(3),"3")
print(IsPrime(4),"4")
print(IsPrime(5), "5")
print(IsPrime(8), "8")
print(IsPrime(89),"89")

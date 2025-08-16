def prime(n,d=3):
    if n==2 or n==3:
        return True
    elif n==1:
        return False
    elif n%2==0:
        return False
    elif n%d==0:
        return False
    elif d>=n//3:
        return True
    else:
        return prime(n,d+2) #general case
        

print(prime(1))
print(prime(2))
print(prime(3))
print(prime(4))
print(prime(5))
print(prime(9))
print(prime(11))
print(prime(49))
print(prime(87))
print(prime(89))

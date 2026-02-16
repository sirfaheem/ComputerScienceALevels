def main():
    print(Factorial(100))

def Factorial(n):
    if n==1 :
        return n
    else:
        return n*Factorial(n-1)


main()

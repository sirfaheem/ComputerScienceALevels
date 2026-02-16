def main():
    print(Fibonacci(5))

def Fibonacci(n):
    if n==1 :
        return n
    else:
        return n+Fibonacci(n-1)


main()

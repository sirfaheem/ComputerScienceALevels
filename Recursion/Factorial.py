def main():
    print(Factorial(100))


def Factorial(n:int):
    if n == 0:
        return 1
    else:
        return n * Factorial(n - 1)


main()

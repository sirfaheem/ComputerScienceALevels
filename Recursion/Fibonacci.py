def main():
    print(Fibonacci(5))


def Fibonacci(n: int):
    if n == 0:
        return 0
    else:
        return n + Fibonacci(n - 1)


main()

def main():
    print(Total())


def Total():
    x = int(input("Enter a number [0, inf) : "))
    if x == 0:  # base
        return x
    return x + Total()


main()

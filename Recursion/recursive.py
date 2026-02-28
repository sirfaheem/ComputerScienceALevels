def main():
    p(5)


def p(a: int):
    print(a)
    if a >= 1:
        p(a - 2)


main()

def main():
    p('faheem')


def p(a: str):
    print(a[-1], end='')
    if len(a) > 1:
        p(a[:-1])


main()

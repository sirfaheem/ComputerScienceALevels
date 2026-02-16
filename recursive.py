def main():
    p(5)

def p(a):
    print(a)
    if a!=1:
        p(a-2)


main()

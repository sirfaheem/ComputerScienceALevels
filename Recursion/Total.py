def main():
    print(Total())

def Total():
    x = int(input("Enter a number [0 to end] "))
    if x==0 : #base
        return x
    else:
        return x+Total()


main()

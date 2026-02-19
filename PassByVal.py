import math

def main():
    m =10
    print(m) #10
    check(m)
    print(m) #10
    assert m == 10

def check(n):
    n+=10
    print(n) #20


main()

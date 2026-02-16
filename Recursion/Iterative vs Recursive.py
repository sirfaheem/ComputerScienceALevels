##def countDown(n):
##    for x in range (n, -1, -1):
##        print(x)


def countDown(n):
    if n !=-1:
        print(n)
        countDown(n-1)
countDown(7)


def CountUp(n):
    for x in range(n+1):
        print(x)

def CountDown(n):
    print(n)
    if n!=1:
      CountDown(n-1)

def ReverseStrRecursive(s):
    print(s[-1], end='')
    if len(s)>1:
        ReverseStrRecursive(s[:-1])

def CountUp(n):
    for x in range(n+1):
        print(x)

def CountDown(n):
    print(n)
    if n!=1:
      CountDown(n-1)

def reverseStr(s):
    rs = ''
    for x in range(len(s)-1, -1, -1):
        rs += s[x]
    return rs



ReverseStrRecursive('faheem')
print()
print(reverseStr('faheem'))
print()
print(CountUp(7))
print()
print(CountDown(7))

def ReverseStrRecursive(s: str) -> str:
    print(s[-1], end='')
    if len(s) > 1:
        ReverseStrRecursive(s[:-1])
    return ""


def reverseStr(s: str) -> str:
    rs = ''
    for x in range(len(s) - 1, -1, -1):
        rs += s[x]
    return rs


def CountUp(n: int):
    for x in range(n + 1):
        print(x)


def CountDown(n: int):
    """
        In the best programming language, this would be (conceptually):
        while (n > 0)
            println (n--);
    """
    if n > 0:
        print(n)
        CountDown(n - 1)


print(ReverseStrRecursive('faheem'))
print(reverseStr('faheem'))
CountUp(7)
CountDown(7)

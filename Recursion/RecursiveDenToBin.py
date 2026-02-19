def DenToBin(n: int):
    b = n % 2
    if n == 0:
        print('0', end='')
    elif n == 1:
        print('1', end='')
    else:
        DenToBin(n // 2)
        print(str(b), end='')


DenToBin(121)

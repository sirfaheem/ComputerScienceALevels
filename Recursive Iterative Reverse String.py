def ReverseStrRecursive(s):
    print(s[-1], end='') #print reverse
    if len(s)>1:
        ReverseStrRecursive(s[:-1])
    #print(s[-1], end='') #print straight



def reverseStr(s):
    rs = ''
    for x in range(len(s)-1, -1, -1):
        rs += s[x]
    return rs



print(ReverseStrRecursive('faheem'))
print()
print(reverseStr('faheem'))




















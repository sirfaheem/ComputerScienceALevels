# binary to denary and hexadecimal

# both not working
def binToDen(b):
    l = len(b)
    d = 0
    p = 0
    for x in range (l):
        p = l-x
        d = d + int(b[x])*2**x
    return d
def binToHex(b): 
    d=0
    h=''
    l = len(b)
    t=''
    for x in range(l-1,-1, -1):
        t+=b[x]
        d = d + int(b[x])*2**x
        if x % 4 == 0:
            if d==10:
                h+='a'
            if d==11:
                h+='b'
            if d==12:
                h+='c'
            if d==13:
                h+='d'
            if d==14:
                h+='e'
            if d==15:
                h+='f'
            else:
                h+=str(d)
            t=''
    return h


b = input('enter a binary number: ')

print(binToDen(b))
print('*'*55)
print(binToHex(b))





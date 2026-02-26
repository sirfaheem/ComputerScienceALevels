def BinToDenary(bs):
    if len(bs) == 0:
        return 0
    if len(bs) == 1:
        return int(bs[0])
    return int(bs[0]) * 2**(len(bs)-1) + BinToDenary(bs[1:])

def BinToDen(bs):
    DenValue=0
    BitValue=0
    Power = len(bs)
    for i in range(len(bs)):
        print(i)
        Bit = bs[i]
        BitValue =  int(Bit)
        Power-=1
        if BitValue==1:
            DenValue = DenValue + 2**Power
            
    return DenValue

value = 0
print(BinToDenary('01000010'))



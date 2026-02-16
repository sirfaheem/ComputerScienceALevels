def BinToDenary(bs):
    if len(bs) == 1:
        return int(bs[0])*2**0
    else:
        return value += BinToDenary(bs[])

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


print(BinToDen('01000010'))



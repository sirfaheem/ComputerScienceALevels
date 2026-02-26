# binary to denary and hexadecimal

def BinToDen(bs:str):
    DenValue=0
    BitValue=0
    Power = len(bs)
    for i in range(len(bs)):
        Bit = bs[i]
        BitValue =  int(Bit)
        Power-=1
        if BitValue==1:
            DenValue = DenValue + 2**Power
            
    return DenValue




b = input('enter a binary number: ')

print(BinToDen(b))
print('*'*55)






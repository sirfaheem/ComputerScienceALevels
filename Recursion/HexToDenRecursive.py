def HexToDen(HexString):
    if len(HexString)==1
        HexDigit = HexString[0]
        if HexDigit == 'a':
            HexValue = 10
        elif HexDigit == 'b':
            HexValue = 11
        elif HexDigit == 'c':
            HexValue = 12
        elif HexDigit == 'd':
            HexValue = 13
        elif HexDigit == 'e':
            HexValue = 14
        elif HexDigit == 'f':
            HexValue = 15
        else:
            HexValue = int(HexDigit)
        ValueSoFar = HexToDen(HexString[1:]) *16 + HexValue
        return ValueSoFar 

print(HexToDen('ff'))

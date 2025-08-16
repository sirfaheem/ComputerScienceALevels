def HexToDen(HexString):
    ValueSoFar = 0
    HexValue = 0
    HexLength =len(HexString)
    i = 0
    HexDigit = ''
    for i in range(HexLength):
        HexDigit = HexString[i]
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
        ValueSoFar = ValueSoFar *16+HexValue
    return ValueSoFar


print(HexToDen('dabba'))






    

MAP: dict[str, int] = {
    'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15,
}

def HexToDen(HexString:str) -> int:
    if len(HexString) == 0:
        raise ValueError('Hex string must not be empty')
    HexDigit = HexString[0]
    HexValue = MAP.get(HexDigit, None)
    if not HexValue:
        HexValue = int(HexDigit)
    if len(HexString) == 1:
        return HexValue
    ValueSoFar = HexToDen(HexString[1:]) * 16 + HexValue
    return ValueSoFar


print(HexToDen('ff'))

HexNum = input("Enter a hexadecimal number: ")
HexNum = HexNum.lower() #convert the uppercase to lowercase
charSet = HexNum in 'abcdef0123456789' #define valid chars

DenNum = 0 #initial denary value
l = len(HexNum) #number of hex digits
print(HexNum)
#HexNum = HexNum[::-1] #reverse the string
HexNum=''
print()
for c in range(l):
    thisChar = HexNum[c:c+1]
    thisDigit = 0
    if thisChar == 'a':
        thisDigit = 10
    elif thisChar == 'b':
        thisDigit = 11

    elif thisChar == 'c':
        thisDigit = 12
        
    elif thisChar == 'd':
        thisDigit = 13
        
    elif thisChar == 'e':
        thisDigit = 14
        
    elif thisChar == 'f':
        thisDigit = 15

    elif thisChar in ('0123456789'):
        thisDigit = int(thisChar)

    DenNum += thisDigit * (16 ** (c))
        
print(DenNum)

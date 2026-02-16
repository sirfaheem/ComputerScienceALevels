hnum = str(input("Enter a hexadecimal number to convert to binary: "))
result = ""

def convh(x):
    global result
    x=x.upper()
    if x == "0":
        result += "0000"
    elif x == "1":
        result += "0001"
    elif x == "2":
        result += "0010"
    elif x == "3":
        result += "0011"
    elif x == "4":
        result += "0100"
    elif x == "5":
        result += "0101"
    elif x == "6":
        result += "0110"
    elif x == "7":
        result += "0111"
    elif x == "8":
        result += "1000"
    elif x == "9":
        result += "1001"
    elif x == "A":# or x == "a":
        result += "1010"
    elif x == "B":
        result += "1011"
    elif x == "C":
        result += "1100"
    elif x == "D":
        result += "1101"
    elif x == "E":
        result += "1110"
    elif x == "F":
        result += "1111"
    else:
        return "Incorrect hexadecimal number"

for char in hnum:
    convh(char)

print(result)
hnum=input()

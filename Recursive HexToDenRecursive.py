def hex_char_to_dec(ch):
    ch = ch.upper()
    
    if ch == 'A':
        return 10
    elif ch == 'B':
        return 11
    elif ch == 'C':
        return 12
    elif ch == 'D':
        return 13
    elif ch == 'E':
        return 14
    elif ch == 'F':
        return 15
    else:
        return int(ch)

def hex_to_dec(hex_str):
    # Base case
    if len(hex_str) == 1:
        return hex_char_to_dec(hex_str)
    
    # General case: multiply first digit by 16^(len-1), add recursion on rest
    return hex_char_to_dec(hex_str[0]) * (16 ** (len(hex_str) - 1)) + hex_to_dec(hex_str[1:])

s = input("Enter Number to convert:")
print("the number in denary:", hex_to_dec(s))

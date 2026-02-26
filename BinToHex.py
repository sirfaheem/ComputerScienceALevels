def binary_to_hex(binary_string):
    # Pad zeros to the left to make length divisible by 4
    padding = (4 - len(binary_string) % 4) % 4
    binary_string = '0' * padding + binary_string
    
    hex_result = ''
    
    # Loop through groups of 4 bits
    for i in range(0, len(binary_string), 4):
        four_bits = binary_string[i:i+4]
        
        # Convert 4-bit group to decimal
        decimal_value = int(four_bits, 2)
        
        # Match statement (Python 3.10+)
        match decimal_value:
            case 0: hex_result += '0'
            case 1: hex_result += '1'
            case 2: hex_result += '2'
            case 3: hex_result += '3'
            case 4: hex_result += '4'
            case 5: hex_result += '5'
            case 6: hex_result += '6'
            case 7: hex_result += '7'
            case 8: hex_result += '8'
            case 9: hex_result += '9'
            case 10: hex_result += 'A'
            case 11: hex_result += 'B'
            case 12: hex_result += 'C'
            case 13: hex_result += 'D'
            case 14: hex_result += 'E'
            case 15: hex_result += 'F'
    
    return hex_result


# Test
print(binary_to_hex('11111111'))  # FF
print(binary_to_hex('1010'))      # A
print(binary_to_hex('1'))         # 1
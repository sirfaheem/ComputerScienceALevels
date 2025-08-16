#convert the program into 2 modules for encryption and decryption#
def encrypt(word , key):
    etext = ''
    for w in range (len (word)):
        e = word [w]
        e = ord(e)
        e = e^ key
        etext += chr(e)
##        print (etext)
    return etext

        
def decryption(etext , key):
    dtext = '' 
    for w in range (len (etext)):
        e = etext [w]
        e = ord(e)
        e = e^ key
        dtext += chr(e)
##        print (dtext)
    return dtext


def main():
    choice = ' '
    cypherText = ''
    while choice.upper() != 'Q':
        choice = (input('Do you want to [E]ncrypt,  [D]ecrypt or [Q]uit: '))
        if choice == 'e' or choice ==  'E':
            word = str(input('Enter anything to encrypt:'))
            key = int(input('Enter the key to your encryption:'))
            cypherText = encrypt(word , key)
            print ('Your data has been Encrypted!!')
        elif choice == 'd' or choice == 'D':
                key = int(input('Enter the key to your decryption:'))
                print (decryption(cypherText , key))
        elif choice == 'Q' or choice == 'q':
                print('Quitting now ... bye bye!')
        else:
            print('invalid option selected')

main()

#decryption/encryption can 0-255 as a key#
###########def main():
##    plainText = input('Please enter text to encrypt')
##    key = int(input('Enter encryption key(between 0-255):'))
##    cypherText = encrypt (plainText, key)
##    if choice == 'e' or 'E':
##        encrypt()
##    elif choice == 'd' or 'D':
##        decrypt()

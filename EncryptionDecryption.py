import random

def main():
    print('''
    1. Generate Key

    2. Encrypt text

    3. Decrypt file

    4. Exit''')

    print()


    while True:
        choice = int(input("Choose an option [1-4]: "))
        if choice == 1:
            genKey()
        elif choice ==2:
            pass
        #ask the user to enter filename and text to encrypt
        elif choice == 3:
            pass
        #ask the user for filename to decrypt and display
        elif choice == 4:
            #exit()
            break
        else:
            print('wrong option selected')

def genKey():
    cypher = ['']*26
    for x in range(26):
        ThisChar = chr(random.randint(65,90))
        while ThisChar in cypher:
            ThisChar = chr(random.randint(65,90))
        cypher[x]=ThisChar
    with open("Key.txt", "w") as fh:
        for x in range(26):
            fh.write(cypher[x]+'\n')
            

main()







        

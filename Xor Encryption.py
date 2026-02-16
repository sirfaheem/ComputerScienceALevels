


def encrypt(filename, userText,password):
    i=0
    NewText=""
    for c in range(len(userText)):
        ThisChar=userText[c]
        ThisChar=ord(ThisChar)
        ThisChar^=ord(password[i])
        NewText+=chr (ThisChar)
        if i==len(password)-1:
            i=0
        else:
            i+=1
                
    with open(filename,"w")as fh:
        fh.write(NewText)
            
def decrypt(filename,password):
    i=0
    dtxt=""

    with open(filename,"r")as fh:
        etxt=fh.read()
        for d in range(len(etxt)):
            ThisChar=ord(etxt[d])
            ThisChar^=ord(password[i])
            dtxt+=chr(ThisChar)
            if i==len(password)-1:
                i=0
            else:
                i+=1


    print(dtxt)
            
def main():
    
    while True:
        print("Encryption/Decryption")
        print("")
    
        print("1.EncryptData")
        print("2.DecryptData")
        print("3.Exit")
        print("")
        print("Select your choice[1-4]")
        Choice=int(input("Enter Your Choice: "))
            
        if Choice==1:
            filename = input("Enter file name: ")
            userText = input("Enter text to encrypt: ")
            password = input("Enter your password: ")
            
            encrypt(filename, userText, password)
        elif Choice==2:
            filename = input("Enter file name: ")
            password = input("Enter your password: ")

            decrypt(filename,password)
            
        elif Choice==3:
            break
        else:
            print("invalid input")

main()








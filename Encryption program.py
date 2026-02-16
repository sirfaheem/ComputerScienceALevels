import random

def genKey():
    print('it will generate a key file')
    key=[""]*26
    
    for i in range(26):
        ThisChar=chr(random.randint(65,90))
        while ThisChar in key:
            ThisChar=chr(random.randint(65,90))    
        key[i]=ThisChar
    with open("Key.txt","w")as fh:
        for x in range(26):
            fh.write(key[x]+"\n")
            
    
def encrypt(filename, userText):
    key=[]
    with open("Key.txt","r")as fh:
        for x in range(26):
            key.append(fh.readline().strip())
    print(key)
    userText=userText.upper()
    NewText=""
    for c in range(len(userText)):
        ThisChar=userText[c]
        ThisChar=ord(ThisChar)-65
        ThisChar=key[ThisChar]
        NewText+=ThisChar
    with open(filename,"w")as fh:
        fh.write(NewText)
            
def decrypt(filename):
    key=[]
    dtxt=""
    with open("Key.txt","r")as fh:
        for x in range(26):
            key.append(fh.readline().strip())
    with open(filename,"r")as fh:
        etxt=fh.read()
        for d in range(len(etxt)):
            ThisChar=etxt[d]
            for a in range(26):
                if key[a]==ThisChar:
                    dtxt+=chr(a+65)
    print(dtxt)
            
def main():
    
    while True:
        print("Encryption/Decryption")
        print("")
        print("1.GenerateKey")
        print("2.EncryptData")
        print("3.DecryptData")
        print("4.Exit")
        print("")
        print("Select your choice[1-4]")
        Choice=int(input("Enter Your Choice: "))
        if Choice==1:
            genKey()
        elif Choice==2:
            filename = input("Enter file name: ")
            userText = input("Enter text to encrypt: ")
            encrypt(filename, userText)
        elif Choice==3:
            filename = input("Enter file name: ")
            decrypt(filename)
        elif Choice==4:
            break
        else:
            print("invalid input")

main()








NULL = -1
#SIZE = 7
SIZE = 4
Data = [""]* SIZE
#Data = ["Hamza", "Abbad", "Faheem", "Ibbad", "Zeeshan", "Muntazir", "Bashir"]
#Next = [3,6,0,5,-1,4,2]
Next = [0] * SIZE
Free = NULL
Start = NULL
Start = 1

def init():
    global Data
    global Next
    global SIZE
    
    for x in range(SIZE):
        Next[x] = x+1
    Next[SIZE-1]=NULL
    
def output():
    global Data
    global Next
    global Start

    idx = Start
    print(Data[idx])
    while Next[idx] !=NULL:
        idx = Next[idx]
        print(Data[idx])

def outputRecursive(Data , Next , idx):
    '''array with data array with pointers'''
    #idx = Start
    if Next[idx]==NULL:
        print( Data[idx])
    else:
        outputRecursive(Data, Next, Next[idx])
        print(Data[idx])
    
def search(val):
    global Data
    global Next
    global Start
    
    isFound = False
    idx = Start
    if Data[idx]==val: isFound=True
    
    while Next[idx] !=NULL:
        idx = Next[idx]
        if Data[idx]==val: isFound=True
    return isFound

def insert(value):
    if Free==SIZE-1:
        print('list is full')
    elif Start==NULL:
        Start = Free
        Data[Free]=value
        Free+=1
        Next[Start]=Free
    else:
        Data[Free] = value
        Temp = Start
        while Temp!=NULL and 
        Free+=1
        
def main():

    #init()
    outputRecursive(Data, Next, Start)
    output()
    print(search("Faheem"))
    print(search("Ali"))

main()

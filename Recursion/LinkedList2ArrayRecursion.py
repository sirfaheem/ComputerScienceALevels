NULL = -1
SIZE = 7
#Data = [""]* SIZE
Data = ["Hamza", "Abbad", "Faheem", "Ibbad", "Zeeshan", "Muntazir", "Bashir"]
Next = [3,6,0,5,-1,4,2]
#Next = [0] * SIZE
Free = 0
#Start = NULL
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
    '''arrat with data array with pointers'''
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
def main():

    #init()
    outputRecursive(Data, Next, Start)
    print()
    output()
    #print(search("Faheem"))
    #print(search("Ali"))

main()

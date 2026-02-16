SIZE = 3
freeListPointer = 0
startPointer = -1
myList=[]
class Node:
    data = ''
    nextP = -1

def initialize():
    global myList
    myList = [Node() for x in range (SIZE)]
    for x in range(SIZE):
        myList[x].nextP = x+1
        myList[x].data="none"
    myList[SIZE-1].nextP=-1

def dump():
    print("data", "next", sep="\t")
    for x in range(SIZE):
        print(myList[x].data, myList[x].nextP, sep="\t")
    print("FreeListPtr: ", freeListPointer, sep="\t")
    print("Start Ptr: ", startPointer, sep="\t")


def printAll():
    thisPtr = startPointer
    while thisPtr != -1:
        print(myList[thisPtr].data, myList[thisPtr].nextP, sep="\t")
        thisPtr = myList[thisPtr].nextP

def insert(s):
    global freeListPointer
    global startPointer
    global myList
    if freeListPointer == -1:
        print('List is full')
    else:
        myList[freeListPointer].Data = s
    if startPointer == -1:
        startPointer = freeListPointer
        Temp = myList[freeListPointer].nextP
        myList[freeListPointer].nextP =-1
        freeListPointer = Temp
    else:
        #traverse the list - starting at start to find
        # the position at which to insert the new item
        Temp = myList[freeListPointer].nextP
        if s < myList[startPointer].data:
            #new item will become the start of the list
            myList[freeListPointer].nextP = startPointer
            startPointer = freeListPointer
            freeListPointer=Temp
        else:
            #the new item is not at the start of the list
            previous = -1
            current = startPointer
            found = False
            while found == False and current !=-1:
                if s <= myList[current].data:
                    myList[previous].nextP = freeListPointer
                    myList[freeListPointer].nextP = current
                    found = True
                else:
                    freeListPointer = Temp
                    #move to the next node
                    previous = current
                    current = myList[current].nextP
            if current==-1:
                myList[previous].nextP = freeListPointer
                myList[freeListPointer].nextP = -1
                freeListPointer = Temp


initialize()
#dump()
insert('faheem')
insert('shafeeq')
insert('qazi')
insert('ali')
insert('not added')

printAll()
#dump()
#myList.insert('faheem')

SIZE = 12 #set the size of the array
NULL = -1
#create a record structure to store a node
class Node:
    Data = ''
    nextP = NULL

#create an array of notes
myList = [Node() for x in range (SIZE)]
#fill the next pointers of array to NULL
for x in range(SIZE):
    myList[x].nextP=x+1
myList[SIZE-1]= NULL
#initialize the heap/free pointer to 0
free = 0
#set start to NULL means list is empty
start = NULL


def insert(value):
    global free
    global start
    global myList

    if free!=NULL:
        myList[free].Data = value
        if start == NULL: #linked list is empty
            start = free
            temp = myList[free].nextP
            myList[free].nextP = NULL
            free = temp
        else: #find the insertion point
            temp = myList[free].nextP
            if value < myList[start].Data:
                #new item becomes the start of the list
                myList[free].nextP = start
                start = free
                free = temp
            else:
                #somewhere in the middle
                prev = NULL
                cur = start
                found = False
                while not found and cur != NULL:
                    if value<=myList[cur].Data:
                        myList[prev].nextP = free
                        myList[free].nextP = cur
                        found = True
                    else:
                        #move to next node
                        free = temp
                        prev = cur
                        cur = myList[cur].nextP

                if cur == NULL:
                    myList[prev].nextP = free
                    myList[free].nextP = NULL
                    free = temp
                    
    else:
        print("list is full")


##def insert(value):
##    global free
##    global start
##    global myList
##    
##    if free==SIZE:
##        print('list full')
##        return
##    #there's space in the array
##    myList[free].Data = value # add new data
##    if start == NULL: #no data in the list      
##        start = free
##    else:
##        #find insertion point
##        T = start
##        prev=NULL
##        while myList[T].Data > value and T !=NULL:
##            prev = T
##            T = myList[T].nextP
##
##        if prev == NULL: #add the node to the beginning
##            myList[T].nextP = start
##            start = T
##        else:
##            myList[T].nextP = myList[prev].nextP
##            myList[prev].nextP = T
##
##    free+=1
            
            

def printAll():
    global start
    global myList
    thisPtr = start
    while myList[thisPtr] != NULL:
        print(myList[thisPtr].Data)
        thisPtr = myList[thisPtr].nextP
def dump():
    global myList
    global free
    global start
    global SIZE
    
    for x in range(SIZE):
        pass
        #print(myList[x].Data, myList[x].nextP, sep="\t")
    #print(myList)
    print("free slot: ", free)
    print("start Pointer: ", start)

##def insert(value):
##        if nextFree == 0:
##            print('List is full')
##        else:
##            Node[nextFree].Data = s
##        if start == 0:
##            start = nextFree
##            temp = Node[nextFree].link
##            Node[nextFree].link =0
##            nextFree = Temp
##        else:
##            #traverse the list - starting at start to find
##            # the position at which to insert the new item
##            Temp = Node[nextFree].link
##            if s < Node[start].data:
##                #new item will become the start of the list
##                nodeNext[free].link = start
##                start = nextFree
##                nextFree.Temp
##            else:
##                #the new item is not at the start of the list
##                previous = 0
##                current = start
##                found = False
##                while found == False and current !=0:
##                    if s <= Node[current].data:
##                        Node[previous].link = nextFree
##                        Node[nextFree].link = current
##                        found = True
##                    else:
##                        nextFree = Temp
##                        #move to the next node
##                        previous = current
##                        current = Node[current].link
##                if current==0:
##                    Node[previous].link = nextFree
##                    Node[nextFree].link = 0
##                    nextFree = Temp
##

insert('habib')
dump()
insert('faheem')
insert('ali')
dump()
insert('zakir')
insert('zainab')
dump()
printAll()



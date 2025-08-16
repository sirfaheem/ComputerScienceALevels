LIST_SIZE = 8
NULL = -1
freeListPtr = 0
startPointer = NULL

class Node:
        data = '' #STRING
        nextP = NULL #INTEGER
thisList = [Node()] 


def init():
    global startPointer
    global freeListPtr
    global thisList
    for x in range (LIST_SIZE):
        thisList.append(Node())
        
    for x in range(LIST_SIZE):
        thisList[x].nextP = x + 1
    thisList[LIST_SIZE-1].nextP = NULL
    freeListPtr = 0 #FreeList points to the first element of the array
    startPointer = NULL #StartPtr is NULL because list is empty.



def insert(s):
    global startPointer
    global freeListPtr
    global thisList
    if freeListPtr != NULL: #List has space for data
        newNodePtr = freeListPtr
        thisList[newNodePtr].data = s
        freeListPtr = thisList[freeListPtr].nextP
        # Find insertion point
        if startPointer == NULL:  # List is empty
            thisList[newNodePtr].nextP = NULL
            startPointer = newNodePtr #becomes 1st element
        else:
            prevPtr = NULL
            thisPtr = startPointer
            while thisPtr != NULL and thisList[thisPtr].data < s:
                prevPtr = thisPtr
                thisPtr = thisList[thisPtr].nextP
                
            if prevPtr == NULL:  # Insert at start of list
                thisList[newNodePtr].nextP = startPointer
                startPointer = newNodePtr
            else:  # Insert in middle or end of list
                thisList[newNodePtr].nextP = thisList[prevPtr].nextP
                thisList[prevPtr].nextP = newNodePtr
    else:
        print('the list is full')

def outputAllNodes():
    global startPointer
    global thisList
    nodePtr = startPointer
    while nodePtr != NULL:
        print(f"{thisList[nodePtr].data} -> ", end="")
        nodePtr = thisList[nodePtr].nextP
    print("None")

def delete(s):
    global startPointer
    global freeListPtr
    global thisList
    if startPointer == NULL:  # List is empty
        print("List is empty, cannot delete node.")
    else:
        prevPtr = NULL
        thisPtr = startPointer
        while thisPtr != NULL and thisList[thisPtr].data != s:
            prevPtr = thisPtr
            thisPtr = thisList[thisPtr].nextP
        
        if thisPtr == NULL:  # Data not found
            print(f"Data '{s}' not found in list.")
        else:
            if prevPtr == NULL:  # Data found at start of list
                startPointer = thisList[thisPtr].nextP
            else:  # Data found in middle or end of list
                thisList[prevPtr].nextP = thisList[thisPtr].nextP
            # Add deleted node to free list
            thisList[thisPtr].data = ''
            thisList[thisPtr].nextP = freeListPtr
            freeListPtr = thisPtr

def search(s):
    global startPointer
    global thisList
    thisPtr = startPointer
    index = NULL
    while thisPtr != NULL:
        index += 1
        if thisList[thisPtr].data == s:
            return index
        thisPtr = thisList[thisPtr].nextP
    return NULL

def dump():
    global startPointer
    global freeListPtr
    global thisList
    print('startPtr: ', startPointer)
    print('freelist: ', freeListPtr)
    for x in range(LIST_SIZE):
        print(x, end=' ')
        print(thisList[x].data, end=' ')
        print(thisList[x].nextP)


init()
dump()
insert('muntazir')
insert('amr')
insert('hamdan')
insert('abbad')
insert('ibad')
insert('hamza')
insert('ibraheem')
insert('faheem')
#insert('ali')
print()
dump()
print()
outputAllNodes()
print('found at : ', search('faheem'))
print('found at : ', search('srihari'))
#insert('asim')
#outputAllNodes()
##delete('qazi')
##delete('abbad')
##dump()
##insert("hadi")
##outputAllNodes()
##print('found at : ', search('qazi'))

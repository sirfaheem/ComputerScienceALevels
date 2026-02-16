class node:
    item = 0
    leftPointer = 0
    rightPointer = 0

SIZE = 8
NULL = -1
myTree = [node()]*SIZE
for x in range(len(myTree)):
    myTree[x].leftPointer = x+1
    myTree[x].rightPointer = NULL
myTree[SIZE-1].leftPointer=NULL

  
rootPointer = NULL
nextFreePointer = 0



oldPointer = 0
itemAdd = 0
itemAddPointer = 0
leftBranch= True

def find(itemSearch):
    global myTree
    global nextFreePointer
    global NULL
    global SIZE
    global rootPointer
    
    itemPointer = rootPointer
    while myTree[itemPointer].item!=itemSearch and (itemPointer!= NULL):
        if myTree[itemPointer].item > itemSearch:
            itemPointer = myTree[itemPointer].leftpointer
        else:
            itempointer = myTree[itemPointer].rightpointer
    return itemPointer

def nodeAdd(itemAdd):
    global myTree
    global nextFreePointer
    global NULL
    global SIZE
    global rootPointer
    
    if nextFreePointer == NULL:
        print("No nodes are free")
    else:
        itemAddPointer = nextFreePointer
        nextFreepointer = myTree[nextFreePointer].leftpointer
        itemPointer = rootPointer
        if itemPointer = NULL:
            rootPointer = itemAddPointer
        else:
            while (itemPointer != NULL)
            oldPointer = itemPointer
            if myTree[itemPointer].item > itemAdd:
                leftBranch = True
                itemPointer = myTree[itemPointer].leftPointer
            else:
                leftBranch = False
                itemPointer = myTree[itemPointer].rightPointer
    if leftBranch:
        myTree[oldPointer].leftpointer = itemAddPointer
    else:
        myTree[oldPointer].rightpointer = itemAddPointer
    myTree[itemAddPointer].leftpointer = NULL
    myTree[itemAddPointer].rightpointer = NULL
    myTree[itemAddPointer].item = itemAdd
itemAdd    

    

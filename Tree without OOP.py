<<<<<<< HEAD
SIZE = 12
NULL = -1
class Node:
    data = 'none'
    leftPtr = NULL
    rightPtr = NULL
tree  = [Node() for x in range (SIZE)]
for c in range(SIZE-1):
    tree[c].rightPtr=c+1


freePtr = 0
rootPtr = NULL
def init():
    
    tree [0].data = "Amr"
    tree[0].leftPtr = 2
    tree[0].rightPtr = 1
    tree [1].data = "Muntazir"
    tree[1].leftPtr = NULL
    tree[1].rightPtr = 4
    tree [2].data = "Ahmed"
    tree[2].leftPtr = 5
    tree[2].rightPtr = 3
    tree [3].data = "Ajmal"
    tree[3].leftPtr = NULL
    tree[3].rightPtr = NULL
    tree [4].data = "Zia"
    tree[4].leftPtr = NULL
    tree[4].rightPtr = NULL
    tree [5].data = "Abbad"
    tree[5].leftPtr = NULL
    tree[5].rightPtr = NULL
    #rootPtr = NULL
    rootPtr = 0
    #self.__freePtr = 0
    freePtr = 6
    #self.__tree[0].data='faheem' #root node assignment

def insert(value):
    global rootPtr
    global freePtr
    if freePtr!=NULL: #has space
        newNodePtr = freePtr
        tree[newNodePtr].data = value
        tree[newNodePtr].leftPtr = NULL
        tree[newNodePtr].rightPtr= NULL
        if rootPtr == NULL:
            rootPtr = newNodePtr
            freePtr+=1
        else:
            thisNodePtr = newNodePtr
            while thisNodePtr!=NULL:
                prevNodePtr = thisNodePtr
                if tree[thisNodePtr].data > value:
                    turnedLeft = True
                    thisNodePtr = tree[thisNodePtr].leftPtr
                else:
                    turnedLeft = False
                    thisNodePtr = tree[thisNodePtr].rightPtr
            if turnedLeft:
                tree[prevNodePtr].leftPtr = newNodePtr
            else:
                tree[prevNodePtr].rightPtr = newNodePtr
                    
    else:
        print('tree is full')

def dump(): #print in original order
    for x in range(SIZE):
        print(tree[x].leftPtr, end=' ')
        print(tree[x].data, end=' ')
        print(tree[x].rightPtr)
    print("Free Pointer: ", freePtr)
    print("Root Pointer: ", rootPtr)
        
def inOrder(root=0):
    if tree[root].leftPtr != NULL:
        inOrder(tree[root].leftPtr)
    print(tree[root].data)
    if tree[root].rightPtr != NULL:
        self.inOrder(tree[root].rightPtr)

def postOrder(self, root=0):
    if tree[root].rightPtr != NULL:
        self.postOrder(tree[root].rightPtr)
    print(tree[root].data)
    if tree[root].leftPtr != NULL:
        self.postOrder(tree[root].leftPtr)

def main():
    dump()
    #init()
    #dump()
    #myData.inOrder()
##    myData.postOrder()
##    print()
    insert("Faheem")
    insert("Saleem")
##    inOrder()
    dump()
    



main()
=======
SIZE = 12
NULL = -1
class Node:
    data = 'none'
    leftPtr = NULL
    rightPtr = NULL
tree  = [Node() for x in range (SIZE)]
for c in range(SIZE-1):
    tree[c].rightPtr=c+1


freePtr = 0
rootPtr = NULL
def init():
    
    tree [0].data = "Amr"
    tree[0].leftPtr = 2
    tree[0].rightPtr = 1
    tree [1].data = "Muntazir"
    tree[1].leftPtr = NULL
    tree[1].rightPtr = 4
    tree [2].data = "Ahmed"
    tree[2].leftPtr = 5
    tree[2].rightPtr = 3
    tree [3].data = "Ajmal"
    tree[3].leftPtr = NULL
    tree[3].rightPtr = NULL
    tree [4].data = "Zia"
    tree[4].leftPtr = NULL
    tree[4].rightPtr = NULL
    tree [5].data = "Abbad"
    tree[5].leftPtr = NULL
    tree[5].rightPtr = NULL
    #rootPtr = NULL
    rootPtr = 0
    #self.__freePtr = 0
    freePtr = 6
    #self.__tree[0].data='faheem' #root node assignment

def insert(value):
    global rootPtr
    global freePtr
    if freePtr!=NULL: #has space
        newNodePtr = freePtr
        tree[newNodePtr].data = value
        tree[newNodePtr].leftPtr = NULL
        tree[newNodePtr].rightPtr= NULL
        if rootPtr == NULL:
            rootPtr = newNodePtr
            freePtr+=1
        else:
            thisNodePtr = newNodePtr
            while thisNodePtr!=NULL:
                prevNodePtr = thisNodePtr
                if tree[thisNodePtr].data > value:
                    turnedLeft = True
                    thisNodePtr = tree[thisNodePtr].leftPtr
                else:
                    turnedLeft = False
                    thisNodePtr = tree[thisNodePtr].rightPtr
            if turnedLeft:
                tree[prevNodePtr].leftPtr = newNodePtr
            else:
                tree[prevNodePtr].rightPtr = newNodePtr
                    
    else:
        print('tree is full')

def dump(): #print in original order
    for x in range(SIZE):
        print(tree[x].leftPtr, end=' ')
        print(tree[x].data, end=' ')
        print(tree[x].rightPtr)
    print("Free Pointer: ", freePtr)
    print("Root Pointer: ", rootPtr)
        
def inOrder(root=0):
    if tree[root].leftPtr != NULL:
        inOrder(tree[root].leftPtr)
    print(tree[root].data)
    if tree[root].rightPtr != NULL:
        self.inOrder(tree[root].rightPtr)

def postOrder(self, root=0):
    if tree[root].rightPtr != NULL:
        self.postOrder(tree[root].rightPtr)
    print(tree[root].data)
    if tree[root].leftPtr != NULL:
        self.postOrder(tree[root].leftPtr)

def main():
    dump()
    #init()
    #dump()
    #myData.inOrder()
##    myData.postOrder()
##    print()
    insert("Faheem")
    insert("Saleem")
##    inOrder()
    dump()
    



main()
>>>>>>> d2ba29fbfd3c554d05834d91472d14f729dcb33b

<<<<<<< HEAD
TSize = 10
NULL = -1
class Node:
    Data = ""
    LeftPtr = NULL
    RightPtr = NULL

Tree = [Node]*TSize
FreePtr = NULL
RootPtr = NULL

def CreateTree():
    RootPtr = NULL
    FreePtr = 0

    for i in range(TSize):
        Tree[i].LeftPtr = i +1
        #Tree[i].RightPtr = NULL
    Tree[TSize-1].LeftPtr = NULL

def AddToTree(ndata):
    #if no space left, give error
    if FreePtr== NULL:
        print('tree is full/no space left')
    else: #add the data in the FreePtr location
        newPtr = FreePtr
        Tree[newPtr].Data = ndata
        #adjust freePtr
        FreePtr = Tree[FreePtr].LeftPtr
        #clear leftPtr
        Tree[newPtr].LeftPtr = NULL
        #is tree currently empty?
        if RootPtr== NULL:
            #make new node, root node
            RootPtr=newPtr
        else:
            #find position to add new node
            index = RootPtr
            FindInsertionPoint(ndata, index, direction)
            if direction=="Left":
                # add new node to the left
                Tree[index].LeftPtr = newPtr
            else:
                # add node to the right
                Tree[index].RightPtr = newPtr

def traverse():
    if ThisPtr != NULL:
        traverse(Tree[ThisPtr].LeftPtr)
        print(Tree[ThisPtr].Data)
        traverse(Tree[ThisPtr].RightPtr)

            
def TraverseTree(root):
    if Tree[root].LeftPtr != NULL:
        TraverseTree(Tree[root].LeftPtr)
    print(Tree[root].Data)
    if Tree[root].RightPtr != NULL:
        TraverseTree(Tree[root].RightPtr)
        



=======
TSize = 10
NULL = -1
class Node:
    Data = ""
    LeftPtr = NULL
    RightPtr = NULL

Tree = [Node]*TSize
FreePtr = NULL
RootPtr = NULL

def CreateTree():
    RootPtr = NULL
    FreePtr = 0

    for i in range(TSize):
        Tree[i].LeftPtr = i +1
        #Tree[i].RightPtr = NULL
    Tree[TSize-1].LeftPtr = NULL

def AddToTree(ndata):
    #if no space left, give error
    if FreePtr== NULL:
        print('tree is full/no space left')
    else: #add the data in the FreePtr location
        newPtr = FreePtr
        Tree[newPtr].Data = ndata
        #adjust freePtr
        FreePtr = Tree[FreePtr].LeftPtr
        #clear leftPtr
        Tree[newPtr].LeftPtr = NULL
        #is tree currently empty?
        if RootPtr== NULL:
            #make new node, root node
            RootPtr=newPtr
        else:
            #find position to add new node
            index = RootPtr
            FindInsertionPoint(ndata, index, direction)
            if direction=="Left":
                # add new node to the left
                Tree[index].LeftPtr = newPtr
            else:
                # add node to the right
                Tree[index].RightPtr = newPtr

def traverse():
    if ThisPtr != NULL:
        traverse(Tree[ThisPtr].LeftPtr)
        print(Tree[ThisPtr].Data)
        traverse(Tree[ThisPtr].RightPtr)

            
def TraverseTree(root):
    if Tree[root].LeftPtr != NULL:
        TraverseTree(Tree[root].LeftPtr)
    print(Tree[root].Data)
    if Tree[root].RightPtr != NULL:
        TraverseTree(Tree[root].RightPtr)
        



>>>>>>> d2ba29fbfd3c554d05834d91472d14f729dcb33b

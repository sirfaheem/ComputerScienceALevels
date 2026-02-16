RootPointer = -1
FreeNode = 0 #INTEGER

ArrayNodes = [[-1 for y in range(3)] for x in range(20)]

def AddNode():
    global ArrayNodes
    global RootPointer
    global FreeNode
    
    Placed = True #Boolean
    CurrentNode = 0
    NodeData = int(input("Enter the data: "))
    if FreeNode <19:
        ArrayNodes[FreeNode][0]= -1
        ArrayNodes[FreeNode][1]= NodeData
        ArrayNodes[FreeNode][2]= -1
        if RootPointer == -1:
            RootPointer = 0
        else:
            Placed = False
            CurrentNode = RootPointer
            while Placed==False:
                if NodeData < ArrayNodes[CurrentNode][1]:
                    if ArrayNodes[CurrentNode][0] == -1:
                        ArrayNodes[CurrentNode][0] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = ArrayNodes[CurrentNode][0]
                else:
                    if ArrayNodes[CurrentNode][2] == -1:
                        ArrayNodes[CurrentNode][2] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = ArrayNodes[CurrentNode][2]
        FreeNode+=1
    else:
        print("Tree is full")

def PrintAll():
    global ArrayNodes
    for r in range(10):
        for c in range(3):
            print(ArrayNodes[r][c], end='\t')
        print()
def InOrder(Root):
    global ArrayNodes
    #ThisNode = Root
    if ArrayNodes[Root][0] != -1:
        InOrder(ArrayNodes[Root][0])
    print(ArrayNodes[Root][1])
    if ArrayNodes[Root][2] != -1:
        InOrder(ArrayNodes[Root][2])

    
 

    
#ArrayNodes, RootPointer, FreeNode
for x in range (10):
    AddNode()

InOrder(RootPointer)
PrintAll()
##print(ArrayNodes)
##print(RootPointer)
##print(FreeNode)
##AddNode()
##AddNode()
##AddNode()

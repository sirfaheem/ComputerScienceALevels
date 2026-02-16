
class node:
    def __init__(self, theData, theNode):
        self.data = theData
        self.nextNode = theNode

def outputNode(linkedList,Ptr):

    if linkedList[Ptr].nextNode==-1:
        return
    else:
        print(linkedList[Ptr])
        outputNode(linkedList, linkedList[Ptr].nextNode)

def main():
    linkedList = [node(1,1), node(5,4), node(6,7),
                  node(7,-1), node(2,2), node(0,6),
                  node(0,8), node(56,3), node(0,9),
                  node(0,-1)]
    startPtr = 0
    emptyList = 5
    outputNode(linkedList, startPtr)

    for x in range(10):
        print(linkedList[x].data,
              linkedList[x].nextNode)

main()

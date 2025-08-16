SIZE = 12

class Node:
    data = ''
    nextP = 0


myList = [Node() for x in range (SIZE)]
for x in range(SIZE):
    myList[x].nextP=x+1
    myList[11].nextP=-1
freeListPointer = 0
startPointer = -1
        

for x in range(SIZE):
    print(self.thisList[x].data, end=' ')
    print(self.thisList[x].nextP)

if self.__freeListPointer!= -1:
    newNodePtr = self.__freeListPointer
    self.__thisList[newNodePtr] = s
    self.__freeListPointer = self.__next[freeListPointer]
    #find insertion point
            

def printAll(self):
    thisPtr = startPointer
    while self.__next != -1:
        print(self.__thisList[thisPtr])
        thisPtr+=1

def insert(self, s):
        if nextFree == 0:
            print('List is full')
        else:
            Node[nextFree].Data = s
        if start == 0:
            start = nextFree
            temp = Node[nextFree].link
            Node[nextFree].link =0
            nextFree = Temp
        else:
            #traverse the list - starting at start to find
            # the position at which to insert the new item
            Temp = Node[nextFree].link
            if s < Node[start].data:
                #new item will become the start of the list
                nodeNext[free].link = start
                start = nextFree
                nextFree.Temp
            else:
                #the new item is not at the start of the list
                previous = 0
                current = start
                found = False
                while found == False and current !=0:
                    if s <= Node[current].data:
                        Node[previous].link = nextFree
                        Node[nextFree].link = current
                        found = True
                    else:
                        nextFree = Temp
                        #move to the next node
                        previous = current
                        current = Node[current].link
                if current==0:
                    Node[previous].link = nextFree
                    Node[nextFree].link = 0
                    nextFree = Temp


myList = linkedList()
myList.dump()
myList.insert('faheem')

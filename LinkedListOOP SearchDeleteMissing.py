class Node:
    def __init__(self, data='', nextPointer =-1):
        self.data = data
        self.nextP = nextPointer

class linkedList:
    def __init__(self, size=12):
        #implement class object
        self.size = size
        self.thisList = [Node() for x in range (self.size)]
        for x in range(self.size-1):
            self.thisList[x].nextP=x+1
        #self.thisList[self.size-1].nextP=-1
        self.__freeListPtr = 0
        self.__startPointer = -1
    def getNextFree(self):
        return self.__freeListPtr
    def dump(self):
        print('startPtr: ', self.__startPointer)
        print('freelist: ', self.__freeListPtr)
        for x in range(self.size):
            print(x, end = ' ')
            print(self.thisList[x].data, end=' ')
            print(self.thisList[x].nextP)

    def insert(self, s):
        
        nextFree = getNextFree()
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
                # the positio at which to insert the new item
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
                                        
                


    def delete(self, s):
        pass
    def printAll(self):
        thisPtr = self.__startPointer
        while self.thisList[self.__startPointer].nextP != -1:
            print(self.__thisList[thisPtr])
            thisPtr+=1

myList = linkedList()
myList.insert('faheem')
myList.dump()
myList.printAll()

LIST_SIZE = 4
class Node:
    def __init__(self):
        self.data = ''
        self.nextP = -1

class linkedList:
    def __init__(self):
        self.thisList = [Node() for x in range(LIST_SIZE)]
        for x in range(LIST_SIZE):
            self.thisList[x].nextP = x + 1
        self.thisList[LIST_SIZE-1].nextP = -1
        self.__freeListPtr = 0
        self.__startPointer = -1

    def dump(self):
        print('startPtr: ', self.__startPointer)
        print('freelist: ', self.__freeListPtr)
        for x in range(LIST_SIZE):
            print(x, end=' ')
            print(self.thisList[x].data, end=' ')
            print(self.thisList[x].nextP)

    def insert(self, s):
        if self.__freeListPtr != -1:
            newNodePtr = self.__freeListPtr
            self.thisList[newNodePtr].data = s
            self.__freeListPtr = self.thisList[self.__freeListPtr].nextP #can we simply incriment?
            # Find insertion point
            if self.__startPointer == -1:  # List is empty
                self.thisList[newNodePtr].nextP = -1 #mark the nextP as end of list
                self.__startPointer = newNodePtr #place the new node at the start
            else:
                prevPtr = -1 #previous is non-existant
                thisPtr = self.__startPointer #start the temp from the startPtr
                while thisPtr != -1 and self.thisList[thisPtr].data < s: #keep moving until the place is found
                    prevPtr = thisPtr
                    thisPtr = self.thisList[thisPtr].nextP
                if prevPtr == -1:  # Insert at start of list (we've checked this earlier)
                    self.thisList[newNodePtr].nextP = self.__startPointer
                    self.__startPointer = newNodePtr
                else:  # Insert in middle or end of list
                    self.thisList[newNodePtr].nextP = self.thisList[prevPtr].nextP
                    self.thisList[prevPtr].nextP = newNodePtr
        else:
            print('the list is full') #this message doesn't show

    def outputAllNodes(self):
        nodePtr = self.__startPointer
        while nodePtr != -1:
            print(f"{self.thisList[nodePtr].data} -> ", end="")
            nodePtr = self.thisList[nodePtr].nextP
        print("None")

    def delete(self, s):
        if self.__startPointer == -1:  # List is empty
            print("List is empty, cannot delete node.")
        else:
            prevPtr = -1
            thisPtr = self.__startPointer
            while thisPtr != -1 and self.thisList[thisPtr].data != s:
                prevPtr = thisPtr
                thisPtr = self.thisList[thisPtr].nextP
            if thisPtr == -1:  # Data not found
                print(f"Data '{s}' not found in list.")
            else:
                if prevPtr == -1:  # Data found at start of list
                    self.__startPointer = self.thisList[thisPtr].nextP
                else:  # Data found in middle or end of list
                    self.thisList[prevPtr].nextP = self.thisList[thisPtr].nextP
                # Add deleted node to free list
                self.thisList[thisPtr].data = ''
                self.thisList[thisPtr].nextP = self.__freeListPtr
                self.__freeListPtr = thisPtr

    def search(self, s):
        thisPtr = self.__startPointer
        index = -1
        while thisPtr != -1:
            index += 1
            if self.thisList[thisPtr].data == s:
                return index
            thisPtr = self.thisList[thisPtr].nextP
        return -1


myList = linkedList()
#myList.dump()
myList.insert('faheem')
myList.insert('zaheer')
myList.insert('qazi')
myList.insert("shafiq")
print('found at : ', myList.search('faheem'))
myList.dump()
myList.delete('shafiq')
myList.insert('ayesha')
myList.outputAllNodes()
myList.delete('qazi')
myList.delete('qazi')
#myList.dump()
myList.outputAllNodes()
print('found at : ', myList.search('qazi'))

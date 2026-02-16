LIST_SIZE = 8
NULL = -1
class Node:
    def __init__(self):
        self.data = '' #STRING
        self.nextP = NULL #INTEGER

class linkedList:
    def __init__(self): #CONSTRUCTOR
        #self.thisList = [Node() for x in range(LIST_SIZE)]
        #DECLARE thisList [0..8]: ARRAY OF Node
        self.thisList = [Node()] 
        for x in range (LIST_SIZE):
            self.thisList.append(Node())
            
        for x in range(LIST_SIZE):
            self.thisList[x].nextP = x + 1
        self.thisList[LIST_SIZE-1].nextP = NULL
        self.__freeListPtr = 0 #FreeList points to the first element of the array
        self.__startPointer = NULL #StartPtr is NULL because list is empty.



    def insert(self, s):
        if self.__freeListPtr != NULL: #List has space for data
            newNodePtr = self.__freeListPtr
            self.thisList[newNodePtr].data = s
            self.__freeListPtr = self.thisList[self.__freeListPtr].nextP
            # Find insertion point
            if self.__startPointer == NULL:  # List is empty
                self.thisList[newNodePtr].nextP = NULL
                self.__startPointer = newNodePtr #becomes 1st element
            else:
                prevPtr = NULL
                thisPtr = self.__startPointer
                while thisPtr != NULL and self.thisList[thisPtr].data < s:
                    prevPtr = thisPtr
                    thisPtr = self.thisList[thisPtr].nextP
                    
                if prevPtr == NULL:  # Insert at start of list
                    self.thisList[newNodePtr].nextP = self.__startPointer
                    self.__startPointer = newNodePtr
                else:  # Insert in middle or end of list
                    self.thisList[newNodePtr].nextP = self.thisList[prevPtr].nextP
                    self.thisList[prevPtr].nextP = newNodePtr
        else:
            print('the list is full')

    def outputAllNodes(self):
        nodePtr = self.__startPointer
        while nodePtr != NULL:
            print(f"{self.thisList[nodePtr].data} -> ", end="")
            nodePtr = self.thisList[nodePtr].nextP
        print("None")

    def delete(self, s):
        if self.__startPointer == NULL:  # List is empty
            print("List is empty, cannot delete node.")
        else:
            prevPtr = NULL
            thisPtr = self.__startPointer
            while thisPtr != NULL and self.thisList[thisPtr].data != s:
                prevPtr = thisPtr
                thisPtr = self.thisList[thisPtr].nextP
            if thisPtr == NULL:  # Data not found
                print(f"Data '{s}' not found in list.")
            else:
                if prevPtr == NULL:  # Data found at start of list
                    self.__startPointer = self.thisList[thisPtr].nextP
                else:  # Data found in middle or end of list
                    self.thisList[prevPtr].nextP = self.thisList[thisPtr].nextP
                # Add deleted node to free list
                self.thisList[thisPtr].data = ''
                self.thisList[thisPtr].nextP = self.__freeListPtr
                self.__freeListPtr = thisPtr

    def search(self, s):
        thisPtr = self.__startPointer
        index = NULL
        while thisPtr != NULL:
            index += 1
            if self.thisList[thisPtr].data == s:
                return index
            thisPtr = self.thisList[thisPtr].nextP
        return NULL

    def dump(self):
        print('startPtr: ', self.__startPointer)
        print('freelist: ', self.__freeListPtr)
        for x in range(LIST_SIZE):
            print(x, end=' ')
            print(self.thisList[x].data, end=' ')
            print(self.thisList[x].nextP)


myList = linkedList()
myList.dump()
myList.insert('muntazir')
myList.insert('amr')
myList.insert('hamdan')
myList.insert('abbad')
myList.insert('ibad')
myList.insert('hamza')
myList.insert('ibraheem')
myList.insert('faheem')
##myList.insert('ali')
##print('found at : ', myList.search('faheem'))

myList.outputAllNodes()
myList.delete('qazi')
myList.delete('hamza')
myList.insert('ali')
myList.delete('faheem')
myList.insert('zaheer')
##myList.dump()
myList.outputAllNodes()
##print('found at : ', myList.search('qazi'))

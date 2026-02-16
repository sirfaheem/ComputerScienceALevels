<<<<<<< HEAD
SIZE = 12
NULL = -1
class Node:
    data = 'none' #string
    leftPtr = NULL #integer 
    rightPtr = NULL #integer
    
class Tree():
    def __init__(self):
        self.__tree  = [Node() for i in range(SIZE)]
##        self.__tree [0].data = "Amr"
##        self.__tree[0].leftPtr = 2
##        self.__tree[0].rightPtr = 1
##        self.__tree [1].data = "Muntazir"
##        self.__tree[1].leftPtr = NULL
##        self.__tree[1].rightPtr = 4
##        self.__tree [2].data = "Ahmed"
##        self.__tree[2].leftPtr = 5
##        self.__tree[2].rightPtr = 3
##        self.__tree [3].data = "Ajmal"
##        self.__tree[3].leftPtr = NULL
##        self.__tree[3].rightPtr = NULL
##        self.__tree [4].data = "Zia"
##        self.__tree[4].leftPtr = NULL
##        self.__tree[4].rightPtr = NULL
##        self.__tree [5].data = "Abbad"
##        self.__tree[5].leftPtr = NULL
##        self.__tree[5].rightPtr = NULL
        #self.__NULL = NULL
        self.__rootPtr = NULL #initialize rootPtr
        #self.__rootPtr = 0
        self.__freePtr = 0
        #self.__freePtr = 6
        #self.__tree[0].data='faheem' #root node assignment

    def dump(self): #print in original order
        for x in range(SIZE):
            print(self.__tree[x].leftPtr, end=' ')
            print(self.__tree[x].data, end=' ')
            print(self.__tree[x].rightPtr)
        print("Free Pointer: ", self.__freePtr)
        print("Root Pointer: ", self.__rootPtr)
        
    def insert(self, sName):
##        newNode = Node()  #if the object is provided as an argument
##        sName = newNode.data =  #keyfield seperated from object
        self.__tree[self.__freePtr].data = sName

        Placed = False
        Temp = self.__rootPtr

        while not Placed:
            if sName < self.__tree[Temp].data:
                if self.__tree[Temp].leftPtr == NULL:
                    self.__tree[Temp].leftPtr = self.__freePtr
                    Placed = True
                else:
                    Temp = self.__tree[Temp].leftPtr
            else:
                if self.__tree[Temp].rightPtr == NULL:
                    self.__tree[Temp].rightPtr = self.__freePtr
                    Placed = True
                else:
                    Temp = self.__tree[Temp].rightPtr
        self.__freePtr +=1
  #convert the code above to recursive
        
  #implement the search method
    def search(self, keyword, root=0):
        if self.__tree[root].data == keyword:
            print('value found')
        elif self.__tree[root].data>keyword and self.__tree[root].leftPtr !=NULL:
            self.search(keyword, self.__tree[root].leftPtr)
        elif self.__tree[root].data<keyword and self.__tree[root].rightPtr !=NULL:
            self.search(keyword, self.__tree[root].rightPtr)
        #print('value not found')
        
  #convert the code below to iterative

        
    def inOrder(self, root=0):
        if self.__tree[root].leftPtr != NULL:
            self.inOrder(self.__tree[root].leftPtr)
        print(self.__tree[root].data)
        if self.__tree[root].rightPtr != NULL:
            self.inOrder(self.__tree[root].rightPtr)

    def postOrder(self, root=0):
        if self.__tree[root].rightPtr != NULL:
            self.postOrder(self.__tree[root].rightPtr)
        print(self.__tree[root].data)
        if self.__tree[root].leftPtr != NULL:
            self.postOrder(self.__tree[root].leftPtr)

def main():
    myData = Tree()
    #myData.dump()
    #myData.inOrder()
    #myData.postOrder() #descending order
    myData.insert("D")
    myData.insert("L")
    myData.insert("A")
    myData.insert("R")
    myData.insert("X")
    print('after adding values \n')
    myData.inOrder() #ascending
    print()
    print(myData.search("R"))
    print(myData.search("B"))



main()
=======
SIZE = 12
NULL = -1
class Node:
    data = 'none' #string
    leftPtr = NULL #integer 
    rightPtr = NULL #integer
    
class Tree():
    def __init__(self):
        self.__tree  = [Node() for i in range(SIZE)]
##        self.__tree [0].data = "Amr"
##        self.__tree[0].leftPtr = 2
##        self.__tree[0].rightPtr = 1
##        self.__tree [1].data = "Muntazir"
##        self.__tree[1].leftPtr = NULL
##        self.__tree[1].rightPtr = 4
##        self.__tree [2].data = "Ahmed"
##        self.__tree[2].leftPtr = 5
##        self.__tree[2].rightPtr = 3
##        self.__tree [3].data = "Ajmal"
##        self.__tree[3].leftPtr = NULL
##        self.__tree[3].rightPtr = NULL
##        self.__tree [4].data = "Zia"
##        self.__tree[4].leftPtr = NULL
##        self.__tree[4].rightPtr = NULL
##        self.__tree [5].data = "Abbad"
##        self.__tree[5].leftPtr = NULL
##        self.__tree[5].rightPtr = NULL
        #self.__NULL = NULL
        self.__rootPtr = NULL #initialize rootPtr
        #self.__rootPtr = 0
        self.__freePtr = 0
        #self.__freePtr = 6
        #self.__tree[0].data='faheem' #root node assignment

    def dump(self): #print in original order
        for x in range(SIZE):
            print(self.__tree[x].leftPtr, end=' ')
            print(self.__tree[x].data, end=' ')
            print(self.__tree[x].rightPtr)
        print("Free Pointer: ", self.__freePtr)
        print("Root Pointer: ", self.__rootPtr)
        
    def insert(self, sName):
##        newNode = Node()  #if the object is provided as an argument
##        sName = newNode.data =  #keyfield seperated from object
        self.__tree[self.__freePtr].data = sName

        Placed = False
        Temp = self.__rootPtr

        while not Placed:
            if sName < self.__tree[Temp].data:
                if self.__tree[Temp].leftPtr == NULL:
                    self.__tree[Temp].leftPtr = self.__freePtr
                    Placed = True
                else:
                    Temp = self.__tree[Temp].leftPtr
            else:
                if self.__tree[Temp].rightPtr == NULL:
                    self.__tree[Temp].rightPtr = self.__freePtr
                    Placed = True
                else:
                    Temp = self.__tree[Temp].rightPtr
        self.__freePtr +=1
  #convert the code above to recursive
        
  #implement the search method
    def search(self, keyword, root=0):
        if self.__tree[root].data == keyword:
            print('value found')
        elif self.__tree[root].data>keyword and self.__tree[root].leftPtr !=NULL:
            self.search(keyword, self.__tree[root].leftPtr)
        elif self.__tree[root].data<keyword and self.__tree[root].rightPtr !=NULL:
            self.search(keyword, self.__tree[root].rightPtr)
        #print('value not found')
        
  #convert the code below to iterative

        
    def inOrder(self, root=0):
        if self.__tree[root].leftPtr != NULL:
            self.inOrder(self.__tree[root].leftPtr)
        print(self.__tree[root].data)
        if self.__tree[root].rightPtr != NULL:
            self.inOrder(self.__tree[root].rightPtr)

    def postOrder(self, root=0):
        if self.__tree[root].rightPtr != NULL:
            self.postOrder(self.__tree[root].rightPtr)
        print(self.__tree[root].data)
        if self.__tree[root].leftPtr != NULL:
            self.postOrder(self.__tree[root].leftPtr)

def main():
    myData = Tree()
    #myData.dump()
    #myData.inOrder()
    #myData.postOrder() #descending order
    myData.insert("D")
    myData.insert("L")
    myData.insert("A")
    myData.insert("R")
    myData.insert("X")
    print('after adding values \n')
    myData.inOrder() #ascending
    print()
    print(myData.search("R"))
    print(myData.search("B"))



main()
>>>>>>> d2ba29fbfd3c554d05834d91472d14f729dcb33b

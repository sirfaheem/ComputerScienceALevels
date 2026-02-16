SIZE = 12
NULL = -1
class Node:
    data = 'none'
    leftPtr = NULL
    rightPtr = NULL
    
class Tree:
    def __init__(self):
        self.__tree  = [Node() for i in range(12)]
        self.__tree [0].data = "Amr"
        self.__tree[0].leftPtr = 2
        self.__tree[0].rightPtr = 1
        self.__tree [1].data = "Muntazir"
        self.__tree[1].leftPtr = NULL
        self.__tree[1].rightPtr = 4
        self.__tree [2].data = "Ahmed"
        self.__tree[2].leftPtr = 5
        self.__tree[2].rightPtr = 3
        self.__tree [3].data = "Ajmal"
        self.__tree[3].leftPtr = NULL
        self.__tree[3].rightPtr = NULL
        self.__tree [4].data = "Zia"
        self.__tree[4].leftPtr = NULL
        self.__tree[4].rightPtr = NULL
        self.__tree [5].data = "Abbad"
        self.__tree[5].leftPtr = NULL
        self.__tree[5].rightPtr = NULL
        self.__NULL = NULL
        self.__rootPtr = NULL
        self.__rootPtr = 0
        #self.__freePtr = 0
        self.__freePtr = 6
        #self.__tree[0].data='faheem' #root node assignment

    def dump(self): #print in original order
        for x in range(SIZE):
            print(self.__tree[x].leftPtr, end=' ')
            print(self.__tree[x].data, end=' ')
            print(self.__tree[x].rightPtr)
        print("Free Pointer: ", self.__freePtr)
        print("Root Pointer: ", self.__rootPtr)
        
    def insert(self, sName):
        newNode = Node()
        newNode.data = sName
        self.__tree[self.__freePtr].data = sName
        self.__tree[self.__freePtr].leftPtr = NULL
        self.__tree[self.__freePtr].rightPtr = NULL
        Placed = False
        Temp = self.__rootPtr

        while not Placed:
            if self.__rootPtr == NULL:
                print("list is empty ... adding first node")
                self.__tree[self.__freePtr] = newNode
                self.__rootPtr = 0
                #self.__freePtr = 1
            else:
                print("Tree not empty ... finding location ")
                placed = False
                while placed == False:
                    if newNode.data < self.__tree[Temp].data:
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
        
    def inOrder(self, root=0):
        if self.__tree[root].leftPtr != self.__NULL:
            self.inOrder(self.__tree[root].leftPtr)
        print(self.__tree[root].data)
        if self.__tree[root].rightPtr != self.__NULL:
            self.inOrder(self.__tree[root].rightPtr)

    def postOrder(self, root=0):
        if self.__tree[root].rightPtr != self.__NULL:
            self.postOrder(self.__tree[root].rightPtr)
        print(self.__tree[root].data)
        if self.__tree[root].leftPtr != self.__NULL:
            self.postOrder(self.__tree[root].leftPtr)

def main():
    myData = Tree()
    #myData.dump()
    #myData.inOrder()
    myData.postOrder()
    myData.insert("Faheem")
    myData.insert("Saleem")
    myData.inOrder()
    



main()

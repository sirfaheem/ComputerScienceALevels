class Node:
    data = 'none'
    leftPtr = 0
    rightPtr = 0
    
class Tree:
    def __init__(self):
        self.__tree  = [Node() for i in range(12)]
        self.__NULL = -1
        self.__rootPtr = -1
        self.__freePtr = 0
        self.__tree[0].data='faheem' #root node assignment

    def dump(self):
        for x in range(12):
            print(self.__tree[x].leftPtr, end=' ')
            print(self.__tree[x].data, end=' ')
            print(self.__tree[x].rightPtr)
        
    def inOrder(self, root):
        if root.leftPtr != self.__NULL:
            inOrder(root.leftPtr)
        print(root.data)
        if root.rightPtr != self.__NULL:
            inOrder(root.rightPtr)

    def postOrder(self, root):
        if root.leftPtr != self.__NULL:
            postOrder(root.leftPtr)
        if root.rightPtr != self.__NULL:
            postOrder(root.rightPtr)
        print(root.data)


def main():
    myData = Tree()
    myData.dump()



main()

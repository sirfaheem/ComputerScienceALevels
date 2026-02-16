TREE_SIZE = 12

class Node:
    data = 'none'
    leftPtr = -1
    rightPtr = -1
    
class Tree:
    def __init__(self):
        self.__tree  = [Node() for i in range(TREE_SIZE)]
        self.__NULL = -1
        self.__rootPtr = -1
        self.__freePtr = 0
        for x in range(TREE_SIZE):
            self.__tree[x].leftPtr = x+1
        self.__tree[TREE_SIZE-1].leftPtr = -1
        self.__tree[TREE_SIZE-1].rightPtr = -1

        #self.__tree[0].data='faheem' #root node assignment

    def dump(self):
        print('root node: ', self.__rootPtr)
        print('free node: ', self.__freePtr)
        for x in range(TREE_SIZE):
            print(self.__tree[x].leftPtr, end=' ')
            print(self.__tree[x].data, end=' ')
            print(self.__tree[x].rightPtr)

    def add_node(self, data):
        # Get the next available node from the free list
        new_node_ptr = self.__freePtr
        if new_node_ptr == -1:
            print("Error: No free nodes available!")
            return

        # Initialize the new node
        self.__freePtr = self.__tree[new_node_ptr].leftPtr
        self.__tree[new_node_ptr].data = data
        self.__tree[new_node_ptr].leftPtr = -1
        self.__tree[new_node_ptr].rightPtr = -1

        # Insert the new node into the tree
        if self.__rootPtr == -1:
            self.__rootPtr = new_node_ptr
        else:
            parent_ptr = -1
            curr_ptr = self.__rootPtr
            while curr_ptr != -1:
                parent_ptr = curr_ptr
                if data < self.__tree[curr_ptr].data:
                    curr_ptr = self.__tree[curr_ptr].leftPtr
                else:
                    curr_ptr = self.__tree[curr_ptr].rightPtr
            if data < self.__tree[parent_ptr].data:
                self.__tree[parent_ptr].leftPtr = new_node_ptr
            else:
                self.__tree[parent_ptr].rightPtr = new_node_ptr

    def inorderPrint(self):
        self.inorder(self.__rootPtr)

    def inorder(self, nodePtr):
        #nodePtr=self.__rootPtr
        if nodePtr != -1:
            self.inorder(self.__tree[nodePtr].leftPtr)
            print(self.__tree[nodePtr].data)
            self.inorder(self.__tree[nodePtr].rightPtr)

  
    def preOrder(self):
        self.__preOrderHelper(self.__rootPtr)
        
    def __preOrderHelper(self, nodePtr):
        if nodePtr != self.__NULL:
            print(self.__tree[nodePtr].data)
            self.__preOrderHelper(self.__tree[nodePtr].leftPtr)
            self.__preOrderHelper(self.__tree[nodePtr].rightPtr)

    def postOrder(self, nodePtr):
        if nodePtr != self.__NULL:
            self.postOrder(self.__tree[nodePtr].leftPtr)
            self.postOrder(self.__tree[nodePtr].rightPtr)
            print(self.__tree[nodePtr].data, end=' ')


##    def __postOrderHelper(self, nodePtr):
##        if nodePtr != self.__NULL:
##            self.__postOrderHelper(self.__tree[nodePtr].leftPtr)
##            self.__postOrderHelper(self.__tree[nodePtr].rightPtr)
##            print(self.__tree[nodePtr].data, end=' ')
##        
    def postOrder1(self):
        self.postOrder(self.__rootPtr)


def main():
    myData = Tree()
    #myData.dump()
    print()
    myData.add_node('faheem')
    myData.add_node('zaheer')
    myData.add_node('qazi')
    myData.add_node('ali')
    myData.dump()
    myData.inorderPrint()
    print()
    myData.preOrder()
    print()
    myData.postOrder1()

main()

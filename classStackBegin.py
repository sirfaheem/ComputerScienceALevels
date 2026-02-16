class Stack:
    def __init__(self, size=10):
        self.__size = size
        self.__array = [''] * size
        self.__tos = size
        self.__full = False
        self.__empty = True

        #create an array of given size
        #initialize the data members
    def push(self, s):
        if self.isFull()==True:
            print('cannot add, stack full')
        else:
            self.__tos -= 1
            self.__array[self.__tos]=s
            print('value added: ', s)
        pass
        #implement the push code
    def pop(self):
        if self.isEmpty()==True:
            s = 'Stack is empty'
        else:
            s = self.__array[self.__tos]
            self.__tos+=1
        #return and remove a string value
        return s
    def isEmpty(self):
        if self.__tos==self.__size:
            self.__empty = True
        else:
            self.__empty = False
        return self.__empty
    def isFull(self):
        if self.__tos<=0:
            self.__full = True
        else:
            self.__full = False
        return self.__full
    def showSize(self):
        return self.__size

def main():
    #write testing program
    nameStack = Stack(2)
    print(nameStack.isEmpty())
    print(nameStack.isFull())
    print(nameStack.showSize())
    nameStack.push('faheem')
    nameStack.push('ali')
    nameStack.push('random')
    print(nameStack.pop())
    print(nameStack.pop())
    print(nameStack.pop())
    nameStack.push('ahmed')
    print(nameStack.pop())
main()

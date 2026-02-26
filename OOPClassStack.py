class Stack():
    def __init__(self,size):
        self.__array = [''] * size
        self.__tos = -1 #initialize tos to null
        self.__size = size

    def push(self,value):
        if self.__tos < self.__size-1:
            self.__tos +=1
            self.__array[self.__tos] = value
        else:
            print("stack is full")

    def pop(self):
        
        t=''
        if self.__tos == -1:
            t = "stack is empty"
        else:
            t = self.__array[self.__tos]
            self.__tos -=1
        return t
myStack = Stack(3)

print(myStack.pop())
myStack.push('E')
myStack.push('C')
myStack.push('A')
myStack.push('Z')
print(myStack.pop())
print(myStack.pop())
print(myStack.pop())
print(myStack.pop())

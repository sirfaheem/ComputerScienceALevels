class Queue():
    def __init__(self, size): #constructor
        self.__size = size #constant size
        self.__array = [''] * size
        self.__head = -1
        self.__tail = -1
        self.__empty = True
        self.__full = False

    def isFull(self):
        if abs(self.__head - self.__tail) == abs(self.__size):
            self.__full = True
        else:
            self.__full = False
        return self.__full
            
    def isEmpty(self):
        #if head and tail are at the same point
        if self.__head == self.__tail :
            self.__empty = True
        else:
            self.__empty = False
        return self.__empty

    def join(self, s:str):
        if self.isFull()==True:
            print('cannot add value')
        else:
            self.__tail+=1
            self.__array[self.__tail]=s
            print('value added successfully')


    def leave(self):
        if self.isEmpty()==True:
            s = 'nothing in queue'
        else:
            self.__head+=1
            s = self.__array[self.__head]
        return s


myQ = Queue(2)
print(myQ.leave()) #should give error
myQ.join('faheem')
myQ.join('ali')
myQ.join('random') # should give error
print(myQ.leave())
print(myQ.leave())
print(myQ.leave()) # should give error

class Node(object):
    def __init__(self,d,n=None):
        self.data = d
        self.next_node = n
    def get_next(self):     #Getter
        return self.next_node
    def set_next(self,n):   #Setter
        self.next_node = n
    def get_data(self):     #Getter
        return self.data
    def set_data(self,d):   #Setter
        self.data=d

class LinkedList(object):
    def __init__(self, r = None):
        self.root = r
        self.size = 0

    def get_size (self):
        return self.size

    def add (self, d):
        new_node = Node (d, self.root)
        if new_node.get_data()>d:
            print("Smaller")
        self.root = new_node
        self.size += 1
        return self.size
###########
##
##def add (self, d):
##        this_node = self.root
##        prev_node = None
##
##        while this_node:
##            if this_node == None or this_node.get_data() <= d :
##                new_node = Node (d, self.root)
##                self.root = new_node
##                self.size += 1
##            elif this_node.get_data()> d:
##                if prev_node:
##                    prev_node.set_next(this_node.get_next())
##                else:
##                    self.root = this_node.get_next()
##                self.size -= 1
##                return True, self.size		# data removed
##            else:
##                prev_node = this_node
##                this_node = this_node.get_next()
###########
    def showList(self):
        node=self.root
        if node.get_next() != None:
            while node:
                print(node.get_data())
                node=node.get_next()
                if node==None:
                    break
            return True
    def remove (self, d):
        this_node = self.root
        prev_node = None

        while this_node:
            if this_node.get_data() == d:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node.get_next()
                self.size -= 1
                return True, self.size		# data removed
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False  # data not found

    def find (self, d):
        this_node = self.root
        while this_node:
            if this_node.get_data() == d:
                return True
            elif this_node.get_next()==None:
                print("Not found")
            else:
                this_node = this_node.get_next()

class mainPrm(object):
    def main(self):
        myList = LinkedList()
        terminate=True
        while terminate:
            UserInput = input("Please enter option code: ")
            while True:
                if UserInput == '1':
                    OutPut = myList.add(int(input("Please enter your data: ")))
                    print(OutPut)
                    uInput=input("Do you wish to continue?(Y/N)")
                    if uInput=='N' or uInput=='n':
                        break
                if UserInput == '2':
                    OutPut = myList.remove(input("Please enter data to be removed: "))
                    print(OutPut)
                    uInput=input("Do you wish to continue?(Y/N)")
                    if uInput=='N' or uInput=='n':
                        break
                if UserInput == '3':
                    OutPut = myList.find(input("Please enter data you wish to find: "))
                    print(OutPut)
                    uInput=input("Do you wish to continue?(Y/N)")
                    if uInput=='N' or uInput=='n':
                        break
                if UserInput == '4':
                    print("Thank You for testing the program!")
                    terminate = False
                    break
                if UserInput == '5':
                    OutPut=(myList.showList())
                    break
                
start = mainPrm()
start.main()
##myList = LinkedList()
##myList.add(5)
##myList.add(8)
##myList.add(12)
##print("size="+str(myList.get_size()))
##myList.remove(8)
##print("size="+str(myList.get_size()))
##print(myList.remove(12))
##print("size="+str(myList.get_size()))
##print(myList.find(50))

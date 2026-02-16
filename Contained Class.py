class Std:
    def __init__(self, n="faheem", a = 5):
        self.name = n
        self.age = a
    def setName(name):
        self.name=name
    def setAge(a):
        self.age=a

class Container:
    def __init__(self, arr):
        self.__arr = arr
    def setData(self, thisStd,i):
        self.__arr[i] = thisStd
        
    def Prn(self):
        for x in range(3):
            print(self.__arr[x].name)



my_object_array = [Std("faheem", 4) for x in range(3)]
myContainer = Container(my_object_array)
object1 = Std("ali",5)
myContainer.setData(object1,2)
myContainer.Prn()

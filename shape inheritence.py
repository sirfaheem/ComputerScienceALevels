<<<<<<< HEAD
class shape():
    def __init__(self):
        self.__name = ""
        self.__area = 0.0
        self.__peri = 0.0
    def showDetails(self):
        print (f'the shape {self.__name} has an area of {self.__area} and')
        print(f'perimeter of {self.__peri}')
    def setName (self, name): #setter
        self.__name = name
    def getName(self): #getter
        return self.__name
    
class square(shape):
    def __init__(self, side):
        self.__side = side
        self.setName("Square")
    def calculate(self):
        self.__area = self.__side * self.__side
        self.__peri = self.__side + self.__side
        self.__peri +=self.__peri

s1 = square(5)
s1.calculate()
s1.showDetails()
=======
class shape():
    def __init__(self):
        self.__name = ""
        self.__area = 0.0
        self.__peri = 0.0
    def showDetails(self):
        print (f'the shape {self.__name} has an area of {self.__area} and')
        print(f'perimeter of {self.__peri}')
    def setName (self, name): #setter
        self.__name = name
    def getName(self): #getter
        return self.__name
    
class square(shape):
    def __init__(self, side):
        self.__side = side
        self.setName("Square")
    def calculate(self):
        self.__area = self.__side * self.__side
        self.__peri = self.__side + self.__side
        self.__peri +=self.__peri

s1 = square(5)
s1.calculate()
s1.showDetails()
>>>>>>> d2ba29fbfd3c554d05834d91472d14f729dcb33b

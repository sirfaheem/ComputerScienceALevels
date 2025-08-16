import datetime

class Person:
    def __init__(self):
        self.name = "none"
        #self.__dob = datetime.date.fromisoformat(input("Enter date in yyyy-mm-dd: "))
        self.__dob = datetime.date.today()
        self.__contactNo = 0
        
    def showData(self):
        #self.__dob.isoformat()
        print (self.name, str(self.__dob), self.__contactNo)
        

class Student(Person):
    def __init__(self):
        super().__init__()
        self.__gpa = 0.0
    def showData (self):
        super().showData()
        print(self.__gpa)
        
s1 = Student()
p1 = Person()

s1.showData()
p1.showData()

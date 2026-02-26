import datetime



class Student():
    def __init__(self, r=0, n='', d=None):
        self.__rollno = r
        self.__name=n
        self.__dob = d
        self.__age = datetime.datetime - d
        
    def output(self):
        print("Roll Number: ", self.__rollno)
        print("Name:        ", self.__name)
        print("Date of Birth:" , self.__dob)
        print("age: ",self.__age)
    

s1 = Student(56, "faheem",datetime.date(2001,5,22))
d = datetime.date(2000,3,21)

s2 = Student(24,'ali',d)

s1.output()
s2.output()

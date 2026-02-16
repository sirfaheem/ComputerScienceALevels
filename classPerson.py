class Person():

    def __init__(self, n, a):
        self.__name = n
        self.age = a
    def ageLater(self):
        return self.age+10
    def getName(self):
        return self.__name
    def setName(self, n):
        self.__name = n

p = Person('Ali', 19)
q = Person('Ahmed', 11)

print(p.getName(), p.age)
print(q.getName(), q.ageLater())

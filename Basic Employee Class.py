class employee:
    def __init__(self, name, staffno):
        self.name = name
        self.staffno = staffno
        self.__salary = 0
    def showDetails(self):
        print("Emp No: ", self.staffno)
        print("Emp Name: ", self.name)
        print("Salary: ", self.__salary)
        print()
    def setSalary(self, sal):
        self.__salary = sal
        
e1 = employee("faheem", 6544)
e2 = employee("srihari", 5943)
e1.setSalary(499)
e2.setSalary(699)


e1.showDetails()
e2.showDetails()


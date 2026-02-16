class employee:
    def __init__(self, name, staffno):
        self.name = name
        self.__staffno = staffno
        self.fullTimeStaff = True

    def showDetails(self):
        print("Staff No: ", self.__staffno)
        print("Employee name: " + self.name)

    def getStaffNo(self):
        return self.__staffno


class partTime(employee):
    def __init__(self, name, staffno):
        employee.__init__(self, name, staffno)
        self.fullTimeStaff = False
        self.__hoursWorked = 0
        self.hourlyRate = 0.0

    def getHoursWorked(self):
        return self.__hoursWorked

    def getHourlyRate(self):
        return self.hourlyRate

    def changeHourlyRate(self, rate):
        self.__HourlyRate = rate

    def addHours(self, hrs):
        self.__hoursWorked += hrs

    def resetHours(self):
        self.__hoursWorked = 0


class fullTime(employee):
    def __init__(self, name, staffno):
        employee.__init__(self, name, staffno)
        self.__fullTimeStaff = 0
        self.__yearlySalary = 0

    def getYearlySalary(self):
        return self.__yearlySalary

    def getMonthlySalary(self):
        return round(self.__yearlySalary / 12, 2)

    def setYearlySalary(self, sal):
        self.__yearlySalary = sal

    def showDetails(self):
        print("Employee Name: ", self.name)
        print("Employee ID: ", self.getStaffNo())
        print("Employee status: Full time")
        print("Yearly salary: ", self.getYearlySalary())
        print("Monthly Salary: ", self.getMonthlySalary())


e1 = employee("Faheem", 3456)
e2 = fullTime("Srihari", 1254)
e3 = partTime("John", 3236)

e1.showDetails()
e2.showDetails()
e3.showDetails()

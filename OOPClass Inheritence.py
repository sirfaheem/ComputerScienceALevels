class employee:
    def __init__(self, name, staffno):
        self.name = name #public attribute
        self.__staffno = staffno #private attribute
        self.__fullTimeStaff = True
    def getEmployeeType(self):
        if self.__fullTimeStaff==True:
            return "Full Time Employee"
        else:
            return "Part Time Employee"
        
    def showDetails(self):
        print("Emp No: ", self.__staffno)
        print("Emp Name: ", self.name)
    def getStaffNo(self):
        return self.__staffno
    def __del__(self):
        print('this object is being deleted.')
class partTime(employee):
    def __init__(self, name, staffno):
        employee.__init__(self, name, staffno)
        self.__fullTimeStaff = False
        self.__hoursWorked = 0
        self.__hourlyRate = 0.0
    def getHoursWorked(self): #getter
        return (self.__hoursWorked)
    def getHourlyRate(self): #getter
        return self.__hourlyRate
    def changeHourlyRate(self, rate): #setter
        self.__HourlyRate = rate
    def addHours(self, hrs):
        self.__hoursWorked+=hrs
    def resetHours(self):
        self.__hoursWorked =0
    def getEarning(self):
        return self.__hourlyRate * self.__hoursWorked
    def showDetails(self):
        employee.showDetails(self)
        print("Hours Worked: ", self.getHoursWorked())
        print("Hourly Rate: ", self.getHourlyRate())
        print("Total Earning: ", self.getEarning())

class fullTime(employee):
    def __init__(self, name, staffno):
        employee.__init__(self, name, staffno)
        self.__fullTimeStaff = True
        self.__yearlySalary = 64000

    def getYearlySalary(self): #getter
        return self.__yearlySalary
    def getMonthlySalary(self): #getter
        return round(self.__yearlySalary/12,2)
    def setYearlySalary(self, sal): #setter
        self.__yearlySalary = sal
    def showDetails(self):
        #employee.showDetails(self)
        print("Employee ID: ", self.getStaffNo())
        print("Employee Name: ", self.name)
        print("Employee Status: Full Time")
        print("Yearly Salary: ", self.__yearlySalary)
        print("Monthly Salary: ", self.getMonthlySalary())
    
e1 = employee("faheem", 6544)
e2 = fullTime("srihari", 5943)
e3 = partTime("sara", 7554)
emp = [None for x in range (3)]
emp[0] = fullTime("ali",55)
emp[0].showDetails()


e1.showDetails()
e2.showDetails()
e3.showDetails()









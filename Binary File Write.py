import pickle
import datetime

class student:
    def __init__(self):
        self.name = ""
        self.regNo = 0
        self.dOB = datetime.datetime.now()
        self.fullTime = True
def writeData():
    
    thisRec = student()
    studentFile = open('students.dat', 'w+b')
    thisRec.name = input("Enter student name: ")
    thisRec.regNo = int(input("Enter Registration No: "))
    day = int(input("enter day for date of birth: "))
    month = int(input("enter month "))
    year = int(input("enter year: "))
    thisRec.dOB = datetime.datetime(year, month, day)
    thisRec.fullTime = bool(input("Full Time? [True/False]"))
    pickle.dump(thisRec, studentFile)
    studentFile.close()

def readData():
    thisRec = student()
    studentFile = open('students.dat', 'rb')
    thisRec = pickle.load(studentFile)
    print(thisRec.name, thisRec.regNo, thisRec.dOB.isoformat())
    studentFile.close()

writeData()
readData()


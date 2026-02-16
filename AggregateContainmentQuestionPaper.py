import os
class Question():
    def __init__(self):
        self.__QText = ''
        self.__Answer = ''
        self.__Marks = 0
    def inputQ(self):
        self.__QText = input('Enter Question Text: ')
        self.__Answer = input('Enter Answer: ')
        self.__Marks = int(input('Enter Marks: '))
    def getAnswer(self):
        return self.__Answer
    def getQText(self):
        return self.__QText
    def getMarks(self):
        return self.__Marks
class QPaper():
    def __init__(self, nq =3):
        self.__NoOfQ = nq
        self.__QArray = [Question] * self.__NoOfQ
    def setQ(self):
        for x in range(self.__NoOfQ):
            self.__QArray[x].inputQ(self)
    def printAll(self):
        os.system("cls")
        for x in range(self.__NoOfQ):
            #print(self.__QArray[x].getQText(self))
            print(f'{self.__QArray[x].getQText(self)}\t[{self.__QArray[x].getMarks(self)}]')

TestP1 = QPaper(1)
TestP1.setQ()
TestP1.printAll()
        

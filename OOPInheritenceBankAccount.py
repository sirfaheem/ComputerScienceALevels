class Test:
    def __init__(self):
        self.__test = None
    def showDetails(self):
        print("this is a test")

class BankAc:
    def __init__(self, acNo, title): #constructor
        self.__acNo = acNo
        self.__accountTitle = title #data member/attribute/field
        self.__balance = 0.0

    def showDetails(self): #method
        print("Account No: ",self.__acNo)
        print("Title of A/c: ",self.__accountTitle)
        print("Balance: ", self.__balance)

class SavingAc(BankAc, Test):
    def __init__(self, no, title, iR):
        BankAc.__init__(self, no, title)
        self.__interestRate = iR
        
    def showDetails(self):
        BankAc.showDetails(self)
        #print("Title: ", self.__accountTitle)
        print("Interest Rate: ",self.__interestRate)
        
    
myAc = SavingAc(3453, "Hadi Khan", 5.6)
myAc2 = BankAc(5584, "SriHari")
myAc.showDetails()


    

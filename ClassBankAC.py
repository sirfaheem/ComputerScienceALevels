class BankAC():
    def __init__(self, t="",acno=0, bal=0):
        self.__title = t
        self.__acNo = acno
        self.__balance = bal
        self.__creationDate = None
        self.__initialDeposit = bal
        self.__acType = ""
    def output(self):
        print("account No: ", self.__acNo)
        print("Title: ", self.__title)
        print("Balance: ", self.__balance)
        print("Account Type:", self.__acType)

    def getBalance(self):
        return self.__balance
    def setBalance(self, b):
        self.__balance = b

    def getDetails(self):
        return self.__acNo, self.__title, self.__balance
    
    def withdraw(self, amount=0):
        if amount>self.__balance:
            print("Limit Exceed!")
        else:
            self.__balance-=amount
            
    def deposit(self, amount=0):
        if amount>=0:
            self.__balance+=amount
        
    
class Savings(BankAC): #inheritence
    def __init__(self, t="",acno=0,
                 init=0, rate=2.5):
        BankAC.__init__(self, t,acno, init)
        BankAC.__acType = "Savings"
        self.__iRate = rate
    def output(self):
        BankAC.output(self) #polymorphism
        print("interest Rate: ", self.__iRate)
    def calculateInterest(self):
        newBal = BankAC.getBalance(self)*self.__iRate
        newBal += BankAC.getBalance(self)
        BankAC.setBalance(self,newBal)
class Current(BankAC):
    def __init__(self, t="",acno=0,  init=0, od=0):
        BankAC.__init__(self, t,acno, init)
        BankAC.__acType = "Current"
        self.__ODLimit = od
    def setODLimit(self, amount):
        self.__ODLimit = amount
    def getODLimit(self):
        return self.__ODLimit
    def output(self):
        BankAC.output(self) #polymorphism
        print("Overdraft Limit: ", self.__ODLimit)
        
ac1 = Savings("faheem", 2341, 2000, 3.5)
ac1.output()
ac1.deposit(1000)
ac1.calculateInterest()
ac1.output()
ac2 = Current("ahmed", 2231, 3000)
ac2.withdraw(50000)
ac2.output()


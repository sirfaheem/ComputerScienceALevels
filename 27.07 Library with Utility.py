import datetime
import random

class LibraryItem:
    def __init__(self, t,a,i):
        self.__Title = t
        self.__AuthorArtist = a
        self.__ItemID = i
        self.__OnLoan = False
        self.__DueDate = datetime.date.today()
        self.__BorrowerID = 0

    def GetTitle(self):
        return (self.__Title)
    def GetAuthorArtist(self):
        return (self.__AuthorArtist)
    def GetItemID(self):
        return (self.__ItemID)
    def Borrow(self, bid):
        self.__BorrowerID = bid
        self.__OnLoan = True
        self.__DueDate = datetime.date.today()+7
    def Return(self):
        self.__BorrowerID = 0
        self.__OnLoan = False
        self.__DueDate = None
        
#lend book
    
    def ShowDetail(self):
        print("ID: ", self.GetItemID())
        print("Title: ", self.GetTitle())
        print("Author: ", self.__AuthorArtist)

class Book(LibraryItem):
    def __init__(self, t, a, i):
        LibraryItem.__init__(self, t, a, i)
        self.__IsRequested = False
        self.__RequestedBy = 0
    def ShowDetail(self):
        LibraryItem.ShowDetail(self)
        #print("is requested: ", self.__IsRequested)
    def SetIsRequested(self, bid):
        self.__RequestedBy = bid

class CD(LibraryItem):
    def __init__(self, t, a, i):
        LibraryItem.__init__(self, t, a, i)
        self.__Genre = ""
    def GetGenre(self):
        return (self.__Genre)
    def SetGenre(self, g):
        self.__Genre = g
class Borrower:
    def __init__(self, n, e):
        self.__BorrowerName = n
        self.__Email = e
        self.__BorrowerID = random.randint(100,200)
        self.__ItemsOnLoan = 0

    def GetBorrowerName(self):
        return self.__BorrowerName
    def GetEmail(self):
        return self.__Email
    def GetBorrowerID(self):
        return self.__BorrowerID
    def GetItemsOnLoan(self):
        return self.__ItemsOnLoan
    def UpdateItemsOnLoan(self):
        self.__ItemsOnLoan += 1
    
    def PrintDetail(self):
        print("ID: ", self.GetBorrowerID())
        print("Name: ", self.GetBorrowerName())
        print("Email: ", self.GetEmail())
        print(f"There are {self.__ItemsOnLoan} items borrowed.")

def Menu():
    choice = 't'
    while choice not in (0,1,2,3,4,5,6,7,8,9):
        print("1 – Add a new borrower")
        print("2 – Add a new book")
        print("3 – Add a new CD")
        print("4 – Borrow a book")
        print("5 – Return a book")
        print("6 – Borrow a CD")
        print("7 – Return a CD")
        print("8 – Request book")
        print("9 – Print all details")
        print("0 – Exit program")

        try:
            choice = int(input("Enter your menu choice: "))
        except ValueError:
            choice = 'a'
        
    return choice

def main():
    Borrowers = []
    Books = []
    CDs = []
    
    choice=Menu()
    while choice != 0:
        if choice==1:
            name =  input("Enter name of borrower ")
            email = input("Enter email of borrower ")
            Borrowers.append(Borrower(name,email))
        elif choice ==2:
            pass
        elif choice==3:
            pass
        elif choice==4:
            pass
        elif choice==5:
            pass
        elif choice==6:
            pass
        elif choice==7:
            pass
        elif choice==8:
            pass
        elif choice==9:
            print(Borrowers[0].GetBorrowerName())
        choice = Menu()

main()        
    ##Title=input("Enter book title: ")
    ##Author = input("Enter book author: ")
    ##ItemID = random.randint(10000, 50000)
##    BookArray = [None for x in range(10)]
    #BookArray[0] = Book(Title, Author, ItemID)

    #BookArray[0].ShowDetail()

##    ThisBook = Book("Harry Potter and Deathly Hallows", "J. K. Rowling", 453)
##
##    ThisBorrower = Borrower("faheem", "faheem@gamil.com")
##    ThisBook.ShowDetail()
##    ThisBorrower.PrintDetail()
##
##

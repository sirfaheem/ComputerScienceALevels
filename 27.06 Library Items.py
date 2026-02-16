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
    pass

##Title=input("Enter book title: ")
##Author = input("Enter book author: ")
##ItemID = random.randint(10000, 50000)
BookArray = [None for x in range(10)]
#BookArray[0] = Book(Title, Author, ItemID)

#BookArray[0].ShowDetail()

ThisBook = Book("Harry Potter and Deathly Hallows", "J. K. Rowling", 453)

ThisBorrower = Borrower("faheem", "sirfaheem@gamil.com")
ThisBook.ShowDetail()
ThisBorrower.PrintDetail()

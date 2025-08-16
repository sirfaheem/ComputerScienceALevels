import datetime

class LibraryItem:
    def __init__(self, t,a,i):
        self.__Title = t
        self.__AuthorArtist = a
        self.__ItemID = i
        self.__OnLoan = False
        self.__DueDate = datetime.date.today()

    def GetTitle(self):
        return (self.__Title)
    def ShowDetail(self):
        print("Title: ", self.GetTitle())
        print("Author: ", self.__AuthorArtist)

class Book(LibraryItem):
    def __init__(self, t, a, i):
        LibraryItem.__init__(self, t, a, i)
        self.__IsRequested = False
        self.__RequestedBy = 0
    def ShowDetail(self):
        LibraryItem.ShowDetail(self)
        print("is requested: ", self.__IsRequested)


ThisBook = Book("Harry Potter and Deathly Hallows", "J. K. Rowling", 453)

print(ThisBook.GetTitle())
ThisBook.ShowDetail()

TempArray = []
CharArray = []
class Character:
    def __init__(self,Namep,Xcoord,Ycoord):
        self.__Name = Namep #Private
        self.__XCoordinate = Xcoord #Private
        self.__YCoordinate = Ycoord #Private

    def GetName(self):
        return self.__Name
    def GetX(self):
        return self.__XCoordinate
    def GetY(self):
        return self.__YCoordinate

    def ChangePosition(self,XChange,YChange):
        self.__XCoordinate = self.__XCoordinate + XChange
        self.__YCoordinate = self.__YCoordinat
    def PrintChar(self):
        print(self.GetName(), self.GetX(), self.GetY())
try:
    with open("Characters.txt",'r') as fh:
        for x in range(30):
            TempArray.append(fh.readline().rstrip())
except:
    print("file not found")

print(TempArray)

for x in range(0,30,3):
    CTemp = Character(TempArray[x], int(TempArray[x+1]), int(TempArray[x+2]))
    CharArray.append(CTemp)
for x in range(10):
    CharArray[x].PrintChar()

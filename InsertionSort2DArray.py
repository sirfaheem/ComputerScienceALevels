#2D Array insertion sort on second column
import random
GlobalArray = [[-1,random.randint(400,500)] for c in range(10)]
NumberOfRecs = 10
Temp0 = 0 #column 1
Temp1 = 0#column 2
Counter = 0 # counter
Placed = False #

print(GlobalArray)

for i in range(0,NumberOfRecs):
    Temp0 = GlobalArray[i][0]
    Temp1 = GlobalArray[i][1]

    Counter = i
    Placed = False
    while (Counter>0) and (not Placed):
        if GlobalArray[Counter-1][1]>Temp1:
            GlobalArray[Counter][0] = GlobalArray[Counter-1][0]
            GlobalArray[Counter][1] = GlobalArray[Counter-1][1]
            Counter-=1
        else:
            Placed = True
    GlobalArray[Counter][0] = Temp0
    GlobalArray[Counter][1] = Temp1    

print(GlobalArray)

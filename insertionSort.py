import random

N = 10
MyList = [random.randint(1,50) for i in range (N)]
#N is upperbound

print(MyList)
Placed = False


#consider all numbers

for index in range(1,N):
    currentValue = MyList[index]
    #find the position in the list to insert
    counter = index
    Placed = False
    while not Placed and counter >0 :
        if currentValue < MyList[counter-1]:
            MyList[counter] = MyList[counter-1]
            counter-=1
        else:
            Placed = True
    MyList[counter] = currentValue



print(MyList)

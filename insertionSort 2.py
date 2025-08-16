import random

N = 7
MyList = [random.randint(1,20) for i in range (N+1)]
#N is upperbound

print(MyList)



#consider all numbers starting with 2nd number

for index in range(1,N):
    currentValue = MyList[index]
    #find the position in the sorted list to insert
    sortedListPosn = 0
    insertPosnFound = False
    while insertPosnFound == False:
        if currentValue>MyList[sortedListPosn]:
            sortedListPosn += 1
        else:
            insertPosn = sortedListPosn
            insertPosnFound = True

    #current value is to move to insertPosn
    # all others on the right shuffle to the right

    for shufflePosn in range(index-1, (insertPosn), -1):
        MyList[shufflePosn] = MyList[shufflePosn-1]
        MyList[insertPosn] = currentValue

print(MyList)

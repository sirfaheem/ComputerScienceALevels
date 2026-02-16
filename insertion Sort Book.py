import random
myList = [random.randint(1,100) for x in range(12)] 
lowerBound = 0
upperBound = len(myList)
print(myList)

for index in range(lowerBound+1, upperBound):
    key = myList[index]
    place = index -1
    if myList[place]>key:
        while place >= lowerBound and myList[place]>key:
            temp = myList[place + 1]
            myList[place+1] = myList[place]
            myList[place] = temp
            place = place -1
        myList[place+1]=key
print(myList)

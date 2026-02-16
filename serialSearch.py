import random
#myList = [0] * 10
#myList = [5,4,87,65,33,13,92,44,76,21]
myList = [random.randint(1,10) for x in range(10) ]
upperBound = 9
lowerBound = 0
index = lowerBound
item = 0
found = False
print(myList)
item = int(input('Enter item to search: '))
while (found == False) and (index <= upperBound):
    if item == myList[index]:        found = True
    index +=1

if found :
    print('found at location ', index)
else:
    print('not found')

import random

upperBound = 9
myList = [random.randint(1, 100) for x in range(upperBound+1)]
myList.sort()

lowerBound = 0
index :int
item = 0
found = False
print(myList)
item = int(input('Enter item to search: '))

while (found == False) and (lowerBound <= upperBound):
    index = (upperBound+lowerBound)//2
    if item == myList[index]:
        found = True
    elif item > myList[index]:
        lowerBound = index + 1
    else:
        upperBound = index - 1
    
if found:
    print('found at location', index)
else:
    print('not found')









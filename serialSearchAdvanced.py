<<<<<<< HEAD
#can do multiple searches
#generate and populate array with 10 random numbers
#use ndArray

import numpy
import random
#myList = [0] * 10
#myList = [5,4,87,65,33,13,92,44,76,21]
myList = [random.randint(1,100) for x in range(upperBound+1) ]

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
=======
#can do multiple searches
#generate and populate array with 10 random numbers
#use ndArray

import numpy
import random
#myList = [0] * 10
#myList = [5,4,87,65,33,13,92,44,76,21]
myList = [random.randint(1,100) for x in range(upperBound+1) ]

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
>>>>>>> d2ba29fbfd3c554d05834d91472d14f729dcb33b

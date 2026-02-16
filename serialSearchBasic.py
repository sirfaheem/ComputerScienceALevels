#can do multiple searches
#generate and populate array with 10 random numbers
#use ndArray

myList = [0] * 10

upperBound = 9
lowerBound = 0
index = lowerBound
item = 0
found = False
print(myList)
item = int(input('Enter item to search: '))
#what's the condition?
while :
    if item == myList[index] : found = True
    index +=1

if found :
    print('found at location ', index)
else:
    print('not found')

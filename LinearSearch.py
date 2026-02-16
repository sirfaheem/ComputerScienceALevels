import random

data = [random.randint(1,20) for x in range (30)]
#print(data)

def LinearSearch(data):
    key = int(input('Enter value to search'))
    found = False

    for x in range (30):
        if key == data[x]:
            print("found at location: ", x)
            found = True

    if found==False:
        print('value not found')

def BubbleSort(data):
    temp = 0
    n = 30 -1
    for i in range (30):
        for j in range(n):
            if data[j]>data[j+1]:
                temp = data[j]
                data[j] = data [j+1]
                data [j+1] = temp
        n = n -1

def InsertionSort(data):
    ItemToBeInserted = 0
    CurrentItem = 0
    index = 0
    
    for index in range(len(data)):
        ItemToBeInserted = data[index]
        CurrentItem = index -1
        while (data[CurrentItem]>ItemToBeInserted and
               CurrentItem>-1):
            data[CurrentItem+1]=data[CurrentItem]
            CurrentItem-=1
        data[CurrentItem+1] = ItemToBeInserted

def BinarySearch(data):
    lowerBound = 0
    upperBound = len(data)-1
    
    key = int(input("Enter value to search: "))
    found = False
    searchFailed = False
    while not searchFailed and not found:
        mid = lowerBound + (upperBound - lowerBound) // 2
        
        if data[mid]==key:
            print('found at location : ', mid)
            found = True
        elif data[mid]>key:
            upperBound =  mid - 1
        else:
            lowerBound = mid + 1 
        if lowerBound > upperBound:
            print('search failed')
            searchFailed = True
      
    if found:
        print(mid)
    else:
        print('value does not exist in the list')

#BubbleSort(data)
InsertionSort(data)
print(data)
BinarySearch(data)














            
  
#LinearSearch(data)
BubbleSort(data)
print(data)

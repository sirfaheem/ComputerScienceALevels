import random
MaxIndex = 12

MyList = [random.randint(1,100) for x in range(MaxIndex)]

print("unsorted")
print(MyList)
print()



def bubbleSortRecursive(myList, n): 
##    if n is None: 
##        n = self.length 
    swapped = False

    # Base case 
    if n == 1: 
        return
    # One pass of bubble sort. After 
    # this pass, the largest element 
    # is moved (or bubbled) to end. 
    for i in range(n - 1): 
        if myList[i] > myList[i + 1]: 
            myList[i], myList[i + 1] = myList[i + 1], myList[i] 
            swapped = True

    # Check if any recursion happens or not 
      # If any recursion is not happen then return 
    if not swapped: 
        return

    # Largest element is fixed, 
    #  recur for remaining array 
    bubbleSortRecursive(myList, n - 1)




bubbleSortRecursive(MyList, 12)



print()
print("sorted")
print(MyList)


##n = MaxIndex -1
##Swapped = True
##i=0
##Temp=0

##while i< MaxIndex-1 and Swapped==True:
##    Swapped = False
##    for j in range(n):
##        if MyList[j] > MyList[j+1]:
##            Temp = MyList[j]
##            MyList[j]=MyList[j+1]
##            MyList[j+1] = Temp
##            Swapped = True
##    n-=1
##    print(MyList)

import random
arr = [random.randint(1,20) for x in range(12)]

print(arr)
maxLimit = len(arr)
n = maxLimit -1
temp = 0
i = 0
Swapped = True
while Swapped == True:
    Swapped = False
    for j in range(n):
        if arr[j]<arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
            Swapped = True
    n-=1

print(arr)    

#visualize
#https://www.geeksforgeeks.org/visualizing-bubble-sort-using-python/

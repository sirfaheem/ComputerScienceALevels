<<<<<<< HEAD
import random
MaxIndex = 12

MyList = [random.randint(1,100) for x in range(MaxIndex)]

print("unsorted")
print(MyList)
print()

n = MaxIndex -1
Swapped = True
i=0
Temp=0

while i< MaxIndex-1 and Swapped==True:
    Swapped = False
    for j in range(n):
        if MyList[j] > MyList[j+1]:
            Temp = MyList[j]
            MyList[j]=MyList[j+1]
            MyList[j+1] = Temp
            Swapped = True
    n-=1
    print(MyList)

print()
print("sorted")
print(MyList)
=======
import random
MaxIndex = 12

MyList = [random.randint(1,100) for x in range(MaxIndex)]

print("unsorted")
print(MyList)
print()

n = MaxIndex -1
Swapped = True
i=0
Temp=0

while i< MaxIndex-1 and Swapped==True:
    Swapped = False
    for j in range(n):
        if MyList[j] > MyList[j+1]:
            Temp = MyList[j]
            MyList[j]=MyList[j+1]
            MyList[j+1] = Temp
            Swapped = True
    n-=1
    print(MyList)

print()
print("sorted")
print(MyList)
>>>>>>> d2ba29fbfd3c554d05834d91472d14f729dcb33b

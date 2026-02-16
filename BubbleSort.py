import random

n = 0
MaxIndex = 10
MyList = [0] * MaxIndex
Temp = 0

#unsorted
print("unsorted list")
for x in range(MaxIndex):
    MyList[x]=random.randint(1,20)
    print(MyList[x])
n = MaxIndex -1

for i in range(MaxIndex-1):
    for j in range(n):
        if MyList[j]>MyList[j+1]:
            Temp = MyList[j]
            MyList[j] = MyList[j+1]
            MyList[j +1]=Temp
    n-=1

print()
print("sorted list")
for x in range(MaxIndex):
    print(MyList[x])

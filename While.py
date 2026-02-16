import random
Size = 10
MyList = []
Swapped = True
x = 0
for c in range(Size):
    MyList.append(random.randint(1,30))
print('unsorted')
print(MyList)

print()

n = Size -1
while Swapped == True:
    Swapped = False
    for j in range(n):
        x+=1
        if MyList[j] > MyList[j + 1]:
            Temp = MyList[j]
            MyList[j] = MyList[j + 1]
            MyList[j + 1] = Temp
            Swapped = True
    n-=1


print(f'sorted in {x} iterations.')
print('sorted')
print(MyList)

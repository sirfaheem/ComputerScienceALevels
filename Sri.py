import random

ArraySize = 10 
MyArray = [0] * ArraySize

Temp = 0.0

for i in range(ArraySize):
    MyArray[i] = round(random.uniform(-10, 39),2)

print("MyArray (Unsorted): ")

print(MyArray)

File1 = open("TData.txt", "w")

for a in range(ArraySize):
    File1.write(str(MyArray[a]) + "\n")
File1.close()

n= ArraySize - 1
for a in range(ArraySize-1):
    for b in range(n):
        if MyArray[b] > MyArray[b + 1]:
            Temp = MyArray[b]
            MyArray[b] = MyArray[b + 1]
            MyArray[b + 1] = Temp
print("MyArray (Sorted): ")
print(MyArray)

File2 = open("CData.txt", "w")


for c in range(ArraySize):
    File2.write(str(MyArray[c]) + "\n")

File2.close()





















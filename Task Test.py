StdArray = []
count = 10
with open("SNames.txt", "r") as f:
    for x in range(10):
        name = f.readline()
        StdArray.append(name.strip())


#print(StdArray[0],count)
t=""
Swapped = True
n=count-1
while Swapped:
    Swapped = False
    for x in range(n):
        if StdArray[x]>StdArray[x+1]:
            t = StdArray[x]
            print(StdArray[x], StdArray[x+1],t)
            StdArray[x] = StdArray[x+1]
            StdArray[x+1]=t
            print(StdArray[x], StdArray[x+1],t)
            print()
            Swapped=True
    n-=1

#print(StdArray[0],n)

with open("Sorted.txt","w") as f:
    for x in range(count):
        f.write(StdArray[x]+"\n")


        

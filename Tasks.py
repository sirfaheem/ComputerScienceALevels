StdArray = []
count = 0
with open("SNames.txt", "r") as f:
    name = f.readline()
    while len(name)>0:
        StdArray.append(name.strip())
        name = f.readline()
        count+=1

print(StdArray[0],count)
t=""
Swapped = True
n=count-2
while Swapped:
    Swapped = False
    for x in range(n):
        if StdArray[x]>StdArray[x+1]:
            t = StdArray[x]
            StdArray[x] = StdArray[x+1]
            StdArray[x+1]=t
            Swapped=True
    n-=1

print(StdArray[0],n)

with open("Sorted.txt","w") as f:
    for x in range(count):
        f.write(StdArray[x]+"\n")


        

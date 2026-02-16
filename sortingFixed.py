<<<<<<< HEAD
numArray = [[0 for x in range(2)] for y in range(10)]
i =0

with open("Characters.txt", "r") as f:
    name = f.readline()
    while len(name)>0:
        x=int(f.readline())
        y=int(f.readline())
        numArray[i][0]=x
        numArray[i][1]=y

        i+=1
        name = f.readline()

n= 10-2
for x in range(10):
    for y in range(n):

        if numArray[y][0]>numArray[y+1][0]:
            #print(numArray[x][0]," ,",numArray[x+1][0])
            t = numArray[y][0]
            numArray[y][0]=numArray[y+1][0]
            numArray[y+1][0] = t

            t = numArray[y][1]
            numArray[y][1]=numArray[y+1][1]
            numArray[y+1][1] = t
    n-=1
for row in range(10):
    for col in range(2):
        print(numArray[row][col], end=" ")
    print()

=======
numArray = [[0 for x in range(2)] for y in range(10)]
i =0

with open("Characters.txt", "r") as f:
    name = f.readline()
    while len(name)>0:
        x=int(f.readline())
        y=int(f.readline())
        numArray[i][0]=x
        numArray[i][1]=y

        i+=1
        name = f.readline()

n= 10-2
for x in range(10):
    for y in range(n):

        if numArray[y][0]>numArray[y+1][0]:
            #print(numArray[x][0]," ,",numArray[x+1][0])
            t = numArray[y][0]
            numArray[y][0]=numArray[y+1][0]
            numArray[y+1][0] = t

            t = numArray[y][1]
            numArray[y][1]=numArray[y+1][1]
            numArray[y+1][1] = t
    n-=1
for row in range(10):
    for col in range(2):
        print(numArray[row][col], end=" ")
    print()

>>>>>>> d2ba29fbfd3c554d05834d91472d14f729dcb33b

nameList = []
##fh = open("SNames.txt","r")
##while len(fh.readline())>0:
##    nameList.append(fh.readline().strip())
##fh.close()

#print(nameList)
filename = input("Enter file name to read: ")
try:
    with open(filename, "r") as fh:
        while len(fh.readline())>0:
            nameList.append(fh.readline().strip())
except FileNotFoundError:
    print("file not found")
for c in range(len(nameList)):
    print(nameList[c])

import random

##f = open("testfile.txt", "a") #r for read, w for write, a for append
##name=input("Enter your name: ")
##age = int(input("Enter your age as a whole number: "))
##rec = name + ","+str(age)+"\n"
##print(rec)
##f.write(rec)
##f.close()

##f = open("testfile.txt", 'r')
##rec = f.readline()
##while (len(rec)>0):
##    print(rec, end='')
##    rec = f.readline()
##f.close()

'''
write a program that will create a 1d array of floats.
assign random numbers between -10 and +39.
write the contents in a file called "TData.txt"
load the contents in another array.
sort the data and write it in a file called "SData.txt"
'''

temp = [0.0] * 30
for x in range(30):
    temp[x] = random.random() *49 - 10

with open("TData.txt", "w") as f:
    for x in range(30):
        f.write(str(temp[x]))

n = 30 - 1
for i in range(30-1):
    for j in range(n):
        if temp[j]>temp[j+1]:
            t = temp[j]
            temp[j]=temp[j+1]
            temp[j+1]=t
    n-=1

print(temp)

with open("SData.txt", "w") as f:
    for x in range(30):
        f.write(str(temp[x]))


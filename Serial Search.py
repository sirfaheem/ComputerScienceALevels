studentNames = ['srihari', 'akash', 'ali', 'nada']
studentMarks = [67,54,62,43]

Found = False
index = 0

name=input("Enter student name to search: ")

while Found==False and index<4:
    if studentNames[index]==name:
        Found = True
    else:
        index+=1

if Found :
    print("name found")
else:
    print("name not found")

<<<<<<< HEAD
Num = 2
StudentArray = [''] * Num
fh = open("StudentDat.txt", 'a')

for x in range(Num):
    name=input('Enter name: ')
    email = input('Enter email: ')
    rec = name+'#'+email
    StudentArray[x] = rec
    fh.write(StudentArray[x]+'\n')

fh.close()
print('Name \t\t\t Email')

for x in range (Num):
    rec=StudentArray[x]
    for i in range(len(rec)):
        if rec[i:i+1]=='#':
            HashPoint = i
    print(rec[:HashPoint] + "\t\t\t " + rec[HashPoint+1:])
=======
Num = 2
StudentArray = [''] * Num
fh = open("StudentDat.txt", 'a')

for x in range(Num):
    name=input('Enter name: ')
    email = input('Enter email: ')
    rec = name+'#'+email
    StudentArray[x] = rec
    fh.write(StudentArray[x]+'\n')

fh.close()
print('Name \t\t\t Email')

for x in range (Num):
    rec=StudentArray[x]
    for i in range(len(rec)):
        if rec[i:i+1]=='#':
            HashPoint = i
    print(rec[:HashPoint] + "\t\t\t " + rec[HashPoint+1:])
>>>>>>> d2ba29fbfd3c554d05834d91472d14f729dcb33b

<<<<<<< HEAD
with open('Numbers.txt', 'w') as nf:
    num = int(input('Enter a number'))
    while num!=0:
        nf.write(str(num)+'\n')
        num = int(input('Enter a number'))

with open('Numbers.txt', 'r') as rf:
    data = rf.readline().strip()
    while len(data)>0:
        data = int(data)
        print(data)
        data = rf.readline().strip()

=======
with open('Numbers.txt', 'w') as nf:
    num = int(input('Enter a number'))
    while num!=0:
        nf.write(str(num)+'\n')
        num = int(input('Enter a number'))

with open('Numbers.txt', 'r') as rf:
    data = rf.readline().strip()
    while len(data)>0:
        data = int(data)
        print(data)
        data = rf.readline().strip()

>>>>>>> d2ba29fbfd3c554d05834d91472d14f729dcb33b

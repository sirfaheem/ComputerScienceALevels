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


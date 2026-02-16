array = [''] * 3

TOS = -1

def push(value):
    global array
    global TOS
    if TOS <len(array)-1:
        TOS=TOS+1
        array[TOS] = value
    else:
        print("stack is full")

def pop():
    global array
    global TOS
    t=''
    if TOS == -1:
        t = "stack is empty"
    else:
        t = array[TOS]
        TOS -=1
    return t

with open('StackData.txt','r') as file:
    data = file.readline().strip()
    while len(data)>0:
        print(data)
        data = file.readline().strip()

    


'''
print(pop())
push('E')
push('C')
push('A')
push('Z')
print(pop())
print(pop())
print(pop())
print(pop())'''

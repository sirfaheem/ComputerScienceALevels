<<<<<<< HEAD
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

print(pop())
push('E')
push('C')
push('A')
push('Z')
print(pop())
print(pop())
print(pop())
print(pop())
=======
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

print(pop())
push('E')
push('C')
push('A')
push('Z')
print(pop())
print(pop())
print(pop())
print(pop())
>>>>>>> d2ba29fbfd3c554d05834d91472d14f729dcb33b

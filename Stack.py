<<<<<<< HEAD
size = 2
stackArray = ['']*size
tos = 0

def push(s):
    global tos
    global size
    global stackArray
    if tos==size:
        print('stack full.')
    else:
        stackArray[tos]=s
        tos+=1
def pop():
    global tos
    global stackArray
    if tos==0:
        print('no data to show')
    else:
        tos-=1
        print(stackArray[tos])

pop()
push('faheem')
push('ali')
push('nadeem')
pop()
pop()
=======
size = 2
stackArray = ['']*size
tos = 0

def push(s):
    global tos
    global size
    global stackArray
    if tos==size:
        print('stack full.')
    else:
        stackArray[tos]=s
        tos+=1
def pop():
    global tos
    global stackArray
    if tos==0:
        print('no data to show')
    else:
        tos-=1
        print(stackArray[tos])

pop()
push('faheem')
push('ali')
push('nadeem')
pop()
pop()
>>>>>>> d2ba29fbfd3c554d05834d91472d14f729dcb33b

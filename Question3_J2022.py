QueueArray = [''] *10 #array of strings
Head:int = 0
Tail:int = 0
NumItems:int = 0

def Enqueue(QueueArray, Head:int, Tail:int, NumItems:int, DataToAdd:str) ->bool: #array of string passed by ref
    if NumItems ==10:
        return False,Head,Tail,NumItems
    QueueArray[Tail]=DataToAdd
    if Tail>= 9:
        Tail=0
    else:
        Tail+=1
    NumItems+=1
    return True,Head,Tail,NumItems

def Dequeue(QueueArray, Head:int, Tail:int, NumItems:int) ->str: #array of string passed by ref
    value = 'Q is empty'
    if NumItems ==0:
        return value,Head,Tail,NumItems


    value = QueueArray[Head]
    if Head>= 9:
        Head=0
    else:
        Head+=1
    NumItems-=1
    return value,Head,Tail,NumItems

success,Head,Tail,NumItems = Enqueue(QueueArray, Head,Tail,NumItems,'36')
print(success,Head,Tail,NumItems,QueueArray)

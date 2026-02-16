QEnd = 2
Array = [""]*QEnd
QSize = 0
Front = 0
Rear = 0

def Join(value):
    global QEnd
    global Rear
    global Array
    global QSize
    if QSize<QEnd:
        Array[Rear]=value
        Rear+=1
        QSize+=1
    else:
        print("Queue is full.")
    if Rear ==QEnd: Rear =0

def Leave():
        global QEnd
        global Front
        global Array
        global QSize
        if QSize<=0:
            value = "Queue is empty"
        else:
            value = Array[Front]
            Front +=1
            QSize-=1
        if Front == QEnd : Front = 0
        return value

Join("Faheem")
Join("Ali")
Join("Kaleem")
print(Leave())
print(Leave())
print(Leave())

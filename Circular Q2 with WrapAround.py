QEnd = 2
Array = [""]*QEnd
QEnd-=1
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
        if Rear==QEnd and QSize<QEnd:
            #wrap around
            Rear=0
    else:
        print("Queue is full.")

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
            if QSize==0 and Front==QEnd:
                Front = 0
        return value

Join("Faheem")
Join("Ali")
print(Leave())
Join("Kaleem")

print(Leave())
print(Leave())

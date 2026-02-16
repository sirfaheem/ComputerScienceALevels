##QSize = 3
##Front = 0
##End  = 0
##NoOfItems = 0
##Q = [""] * QSize
##
##def InitializeQ():
##    global Front
##    global End
##    global NoOfItems
##    Front = -1
##    End = -1
##    NoOfItems = 0
##
##def join(n):
##    global Front
##    global End
##    global NoOfItems
##    global Q
##    global QSize
##    if NoOfItems < QSize:
##        End +=1
##        if End > QSize-1:
##            End = -1
##        Q[End] = n
##        NoOfItems += 1
##    else:
##        print('Q is full')
##            
##def leave():
##    global Front
##    global End
##    global NoOfItems
##    global Q
##    global QSize
##    Item = ""
##    if NoOfItems > 0:
##        Item = Q[Front]
##        NoOfItems -= 1
##        if NoOfItems==0:
##            InitializeQ()
##        else:
##            Front = Front +1
##            if Front>QSize-1:
##                Front = -1
##    else:
##        print('Q is empty')
##    return Item
##        
##join('A')
##join('B')
##join('C')
##join('D')
###join ('E')
##print(leave())
##print(leave())
##print(leave())

Q_SIZE = 3
front = 0
end = 0
no_of_items = 0
q = [""] * Q_SIZE

def initialize_q():
    global front
    global end
    global no_of_items
    front = 0
    end = 0
    no_of_items = 0

def join(n):
    global front
    global end
    global no_of_items
    global q
    global Q_SIZE
    if no_of_items < Q_SIZE:
        end += 1
        if end == Q_SIZE:
            end = 0
        q[end] = n
        no_of_items += 1
    else:
        print('Q is full')

def leave():
    global front
    global end
    global no_of_items
    global q
    global Q_SIZE
    item = ""
    if no_of_items > 0:
        item = q[front]
        no_of_items -= 1
        if no_of_items == 0:
            initialize_q()
        else:
            front += 1
            if front == Q_SIZE:
                front = 0
    else:
        print('Q is empty')
    return item

join('A')
join('B')
join('C')
join('D')
print(leave())
print(leave())
print(leave())
print(leave())


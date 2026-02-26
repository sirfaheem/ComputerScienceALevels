front = 0
back = 0
Queue = ['']*4
size=0
def join(person):
    global front
    global back
    global Queue
    global size
    if size>=len(Queue):
        print('q full')
    else:
        
        Queue[back]=person
        if back==len(Queue)-1:
            back=0
        else:
            back+=1
        size+=1
    
def leave():
    global front
    global back
    global Queue
    global size
    if size<=0:
        return 'queue is empty'
    else:
        person = Queue[front]
    
        if front==len(Queue)-1:
            front=0
        else:
            front+=1
        size-=1
    
    
    return person

join('ali')
join('anand')
join('srihari')
join('faheem')
print(leave())
join('david')
print(leave())
print(leave())
print(leave())
print(leave())

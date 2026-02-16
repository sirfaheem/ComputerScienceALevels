Q = [''] * 3

front = 0
end = 0
MaxQSize = len(Q)

def join(value):
    global Q
    global end
    global MaxQSize
    if end<MaxQSize:
        Q[end] = value
        end+=1
        print(value, 'joined')
    else:
        print('Q is full')

def leave():
    t = ''
    global Q
    global MaxQSize
    global front
    if front == MaxQSize:
        t = 'nothing to show'
    else:
        t = Q[front]
        front+=1
    return t

#print(leave())
join('E')
join('C')
join('A')
join('Z')
print(leave())
print(leave())
print(leave())
print(leave())

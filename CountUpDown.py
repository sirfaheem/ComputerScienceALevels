def countUp():
    for x in range(1,11):
        print(x)
def countDown():
    for x in range(10,0, -1):
        print(x)

def countRec(n):
    if n>0: #general case
        print(n)
        countRec(n-1)
    else:           #base case
        return
    
countRec(6)

x=int(input("enter number to convert to binary"))
def con(x):
    if x==0:
        return x
    elif x>1:
        return str(con(x//2))+str(x%2)
    else:
        return "1"

print(con(x))
x=input()

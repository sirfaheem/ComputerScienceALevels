
def underoot(num ): #by val
    num = 36
    return num **0.5

def modify(arr): #byref
    arr.append(6)
    #return arr




array = [5]*2
print(array)
modify(array)
print(array)
n = 25

print(underoot(n))

print(n)
n = underoot(n)
print(n)


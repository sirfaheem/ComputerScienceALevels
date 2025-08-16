global userCount
userCount= 0

def greetMe(username):
    global userCount
    userCount+=1
    print("hello " + username + str(userCount))


def underoot(num ): #by val
    num = 36
    return num **0.5

def modify(arr): #byref
    arr.append(56)
    return arr


greetMe('anonymous')
greetMe('saif')
greetMe('faheem')

print(userCount)
##array = [5]*2
##print(array)
##modify(array)
##print(array)
##n = 25
##print(underoot(n))
##print(n)



def greetMe(name):
    n = 1 #local variable
    global userCount
    userCount+=1
    print('hello '+ name +str(userCount))


global userCount
userCount = 0 #global 
greetMe('faheem')
greetMe('SriHari')
greetMe('Brenda')

print(userCount)




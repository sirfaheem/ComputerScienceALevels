##n = t = c = 0
###10, 20, 0
##n = int(input("Enter a number [0 to end]: "))
##
##while n!=0 :
##    t = t+ n
##    c = c+1
##    n = int(input("Enter a number [0 to end]: "))
##
##print(t/c)

n = int(input("Enter a number [0 to end]: "))
Max = n
Min = n

while n !=0:
    if n>Max : Max = n
    n = int(input("Enter a number [0 to end]: "))
print ("the largest number is : ", Max)

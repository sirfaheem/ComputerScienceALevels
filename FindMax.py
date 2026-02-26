n = int(input("Enter a number [0 to end]: "))
Max = n
Min = n

while n !=0:
    if n>Max : Max = n
    n = int(input("Enter a number [0 to end]: "))
print ("the largest number is : ", Max)

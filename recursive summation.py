
#modify this program to return average
def summation():
    n = int(input("Enter number: "))
    if n ==0 :
        return n
    else:
        return n + summation()


print(summation())

a = 0
b=1

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
except ValueError, TypeError:
    print("please enter a valid integer number")
c=0
try:
    c = a/b
except NameError:
    print()
except ZeroDivisionError:
    print("cannot divide by zero")


print(c)

x = 1

def calcArea(side):
    global x
    x+=2
    print(x)
    return side * side

def main():
    global x
    #shape = input('Enter shape to find area [circle, rectangle]')
    
    length = int(input("Enter the length of a side "))
    area = calcArea(length)
    print(area)
    print(x)

main()

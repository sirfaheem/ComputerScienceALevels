def main():
    print('''Calculate area and perimeter
             1. Circle
             2. Rectangle
             3. Exit
             Type an option [1..3]
             ''')
    chioce = input()
    try:
        choice = int(choice)
    except:
        print('please enter a valid option')
    if choice == 1:
        circle()
        print("Circle option works")
    elif choice ==2:
        rectangle()
    elif choice == 3:
        exit()
    else:
        print("invalid input")

def circle():
    pass

def rectangle():
    print("rectangle function works.")

main()


decision = 'y'

while decision.lower()!='n':
    bun_price = float(0.50)
    coffee_price = float(1.20)
    cake_price = float(1.50)
    sandwich_price = float(2.10)
    dessert_price = float(4.00)

    bun_current = 0
    coffee_current = 0
    cake_current = 0
    sandwich_current = 0
    dessert_current = 0

    bun_final = float()
    coffee_final = float()
    cake_final = float()
    sandwich_final = float()
    dessert_final = float()

    total_products_for_day = 0

    x = 0

    item = ()

    count = 0
    num = int(input("How many items? "))

    while count < num:
        item = input("Enter the item: ")
        if item == ("bun"):
            bun_current + 1
        elif item == ("coffee"):
            coffee_current + 1
        elif item == ("cake"):
            cake_current + 1
        elif item == ("sandwich"):
            sandwich_current + 1
        elif item == ("dessert"):
            dessert_current + 1
        count+=1 # must increment

    bun_final = bun_price * bun_current
    coffee_final = coffee_price * coffee_current
    cake_final = cake_price * cake_current
    sandwich_final = sandwich_price * sandwich_current
    dessert_final = dessert_price * dessert_current   

    total_products_for_day = bun_current + coffee_current + cake_current + sandwich_current + dessert_current

    total_price = bun_final + coffee_final + cake_final + sandwich_final + dessert_final

    print("Total price is " + total_price)

    decision = input("Next customer?(y/n) ")

        

print(total_products_for_day)

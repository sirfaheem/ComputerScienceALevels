bun_p = 0.50
coffee_p = 1.20
cake_p = 1.50
sandwich_p = 2.10
dessert_p = 4.00

bun_c = 0
coffee_c = 0
cake_c = 0
sandwich_c = 0
dessert_c = 0

bun_f = 0
coffee_f = 0
cake_f = 0
sandwich_f = 0
dessert_f = 0

next = input ("End program?(y/n) ")
if next == ("y"):
    input("Press enter to end program")
    sys.exit()
else:
    while next == ("n"):

        quant = int(input("How many items? "))
        count = 0

        while count<quant:
            item = input("Enter the item: ")
            count+=1
            if item == ("bun"):
                bun_c += 1
            elif item == ("coffee"):
                coffee_c += 1
            elif item == ("cake"):
                cake_c += 1
            elif item == ("sandwich"):
                sandwich_c += 1
            elif item == ("dessert"):
                dessert_c += 1

            

        total_price = bun_c * bun_p + coffee_c * coffee_p + cake_c * cake_p + sandwich_c * sandwich_p + dessert_c * dessert_p

        print("Total price is $" + str(total_price))

        next = input("End program? (y/n) ")

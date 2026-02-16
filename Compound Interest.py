#f = p*(1+i)**t
# f is the future value
# p is present value
# i is the monthly interest rate
# t is the number of months

p=float(input("Enter the money you have right now: "))
i=float(input("Enter the current interest rate: "))
t = int(input("Enter number of months: "))

f = p*(1+i)**t

print(f"your future value is: {f:.2f}")

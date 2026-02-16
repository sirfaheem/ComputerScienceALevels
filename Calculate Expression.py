def Calculate(Exp):
    Num1 = ""
    Num2 = ""
    Op = '.'
    for c in range(len(Exp)):
        ThisChar = Exp[c:c+1]
        if ThisChar in ('+','-','/','*'):
            Op = ThisChar
            Num1=Exp[0:c]
            Num2=Exp[c+1:]
        #elif Op=='.':
           # Num1+=ThisChar
        #else:
            #Num2+=ThisChar
    Num1 = int(Num1)
    Num2 = int(Num2)

    if Op=='+': print(Num1+Num2)
    if Op=='-': print(Num1-Num2)
    if Op=='/': print(Num1/Num2)
    if Op=='*': print(Num1*Num2)

Calculate("23/2")
Calculate("23+98")

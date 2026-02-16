def main():
    print(HCF(75,30))
    print(GCD(75,30))

def HCF(n1,n2):
    if n2!=0 :
        return HCF(n2,n1%n2)
    else:
        return n1

def GCD(n1,n2):
    while n2!=0:
        r = n1 %n2
        n1=n2
        n2 = r
    return n1
main()

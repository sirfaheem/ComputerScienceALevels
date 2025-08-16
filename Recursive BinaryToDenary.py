def DenToBin(n):    #recursive
    if n==0  or n==1: #base case
        print(n,end='')
    else:           #general case
        DenToBin(n//2)
        print(n % 2, end='')

def DenToBinary(n): #iterative solution
    s = ''
    while n !=0:
        s=str(n%2)+s
        n//=2
    print(s)

if __name__ == "__main__":
    DenToBin(1120)
    print()
    DenToBinary(1120)

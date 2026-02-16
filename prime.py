
n = int(input('Enter a number: '))
prime = True
div = 3

if n==1:
    prime=False
    
while (div<=(n/2) and prime == True):
    if n%div==0:
        prime=False
    else:
        div+=1
if prime == True:
    print('Prime')
else:
    print('Composite')

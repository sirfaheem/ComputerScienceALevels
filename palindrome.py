pCount=0
for x in range (5):
    num = input("Enter a 4 digit number: ")
    if len(num)==4:
        if num[0:1]==num[3:] and num[1:2] == num[2:3]:
            pCount +=1
##            print("it is a palindrome")
##        else:
##            print("it is not a palindorme")
##    else:
##        print('the entered text is not 4 digits')

print(f'there were {pCount} palindromes')

ans = 'y'

while upper(ans)=='Y':
    ans =  input('do you want to continue [y/n]?')

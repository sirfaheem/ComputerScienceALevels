text = input('Enter text: ')
#text = 'this is a sample text'
aCount = 0
for x in range(len(text)):
    if text[x] in ('a','e','i','o','u'):
        aCount +=1
print(aCount)

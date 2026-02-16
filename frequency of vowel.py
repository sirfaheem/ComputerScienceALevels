text = input('Enter text: ')
text = 'this is a sample text'
aCount = 0
for x in range(len(text)):
    if text[x:x+1]=='s':
        aCount +=1
print(aCount)

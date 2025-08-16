''' write a program as a module that accepts some text and returns the hieghest
frequencey letter in that text. '''

def hfreq(text):
    alpha = [0]*26
    text = text.upper()
    for c in range (len(text)):
        loc = ord(text[c])
        loc-=65
        if loc>=0:
            alpha[loc]+=1
    hf=alpha[0]
    letter = 65
    for x in range(len(alpha)):
        if alpha[x]>hf:
            hf=alpha[x]
            letter=x+65
    return chr(letter)















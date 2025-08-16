text = input("Enter text")
occurences = [0]*26


def frequency(text, occurences):
    z = 0
    loc = 0

    text=text.upper()
    for i in range(len(text)):
        position = (ord(text[i]) - 65)
        if position>=0:
            occurences[position]+=1
        

    return occurences



print(frequency(text,occurences))



















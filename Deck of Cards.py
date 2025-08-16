Deck = [[ "" for x in range(14)] for y in range(4)] # one empty row at the top
#Deck[0] = ['spades','heart', 'diamond', 'club']
suits = ['\u2660', '\u2665', '\u2666', '\u2663'] #filled symbols
suit = ['\u2664', '\u2661', '\u2662', '\u2667'] #empty outline
for x in range(4):
    
    for y in range(1,14):

        if y == 1 : Deck[x][y] = suit[x] + " Ace"
        elif y == 11 : Deck[x][y] = suit[x] + " Jack"
        elif y == 12 : Deck[x][y] = suit[x] + " Queen"
        elif y == 13 : Deck[x][y] = suit[x] + " King"
        else:
            Deck[x][y] = suit[x] + " " + str(y)            
print(Deck)
print(suit)

for d in range(4):
    card='\u1f0a'+d #u1f0a1, u1f01b1, u1f0c1, u1f0d1
for x in range(14):
    print(card+str(x)) #u1f0a1, u1f0a2, u1f0a3

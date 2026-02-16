deck = [[x for x in range(4)] for rank in range(15)]
#suits = ['diamond', 'spade', 'hearts', 'ace']
'''•'''
suits = [ '0xa8', '0xa9', '0xaa']
for row in range(4):
    deck[0][row] = suits[row]
    
for row in range(15):
    for suits in range(4):
        print(deck[row][suits], end='\t')
    print()
print('-'*25)
for col in range(1,15):
    for suit in range(4):
        deck[col][suit] = col
        if col==10:
            deck[col][suit] = 'A'
        elif col==11:
            deck[col][suit] = 'J'
        elif col==12:
            deck[col][suit] = 'Q'
        elif col==13:
            deck[col][suit] = 'K'

for row in range(14):
    for suits in range(4):
        print(deck[row][suits], end='\t')
    print()




##def main():
##    initGame()
##    drawHand()
##    drawHand()
##    while gameEnd=False:
##        
##        showHand()
##        checkBusted()
##        if busted:
##            gameEnd=True
##        else:
##            userChoice = inputChoice()
##            match userChoice:
##                case 'd':
##                    print('draw a card')
##                    drawHand()
##                case 'c':
##                    print('player calls')
##                    checkWinner()
##                case 'q':
##                    print('quit the game')
                
    




        

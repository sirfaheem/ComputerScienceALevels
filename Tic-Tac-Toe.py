BLANK = '.'
board = [[BLANK for col in range(3)] for row in range(3)] #game grid

def main():
    initBoard() #initialize /reset Board
    thisPlayer, gameEnd = setup()     #SetupGame
    outputBoard()
    while gameEnd==False:
        row, col = playerMakesMove(board, thisPlayer) #playerMakesMove
        outputBoard()
        gameEnd = checkGameEnd(board, thisPlayer, row, col, gameEnd)
        if gameEnd==False:
            thisPlayer = swapPlayer(thisPlayer)

def checkGameEnd(board, thisPlayer, row, col, gameEnd):
    winnerFound = False
    winnerFound = checkIfPlayerHasWon(board, thisPlayer, row, col, winnerFound)
    if winnerFound == True:
        gameEnd = True
        print(thisPlayer + ' has won')
    else:
        gameEnd = checkForFullBoard(board, gameEnd)
    return gameEnd
        
def checkIfPlayerHasWon(board, thisPlayer, row, col, winnerFound):
    winnerFound = checkHorizontalLine(board, thisPlayer, row, winnerFound)
    if winnerFound==False:
        winnerFound = checkVerticalLine(board, thisPlayer, col, winnerFound)
        if winnerFound==False:
            winnerFound = checkDiagnol(board, thisPlayer, row, col, winnerFound)

    return winnerFound

def checkForFullBoard(board, gameEnd):
    blankFound = False
    thisRow = -1
    thisCol = 0
    while thisRow<6 and blankFound==False:
        thisCol=-1
        thisRow+=1
        while thisCol<7 and blankFound==False:
            thisCol+=1
            if board[thisRow][thisCol] == BLANK:
                blankFound=True
    if blankFound==False:
        print("it's a draw")
        gameEnd=True

    return gameEnd


def initBoard():
    for row in range(3):
        for col in range(3):
            board[row][col]=BLANK
def setup():
    #global gameEnd
    thisPlayer = 'O'
    gameEnd=False
    return thisPlayer, gameEnd

def outputBoard():
    print('''TIC-TAC-TOE ''')
    print('',end='\t')
    for heading in ('A', 'B', 'C'):
        print( heading, end='\t')
    print()
    for row in range(2,-1,-1):
        print(str(row+1), end='\t')
        for col in range(3):
            print(board[row][col], end='\t')
        print()
        print()

def playerMakesMove(board, thisPlayer):
    validMove = checkMove(board, thisPlayer)
    validRow = playerChoosesRow(board, thisPlayer)
    board[validRow][validCol] = thisPlayer
    return validRow, validCol

def checkMove(board, thisPlayer):
    move = input('Enter move: [eg. A2 for center]')
    if len(move)!=2 or move[0] not in ('A', 'B', 'C') \
       or move[1] not in (1,2,3) or board[row][col]!=BLANK:
        return False
    else:
        return True
    
def swapPlayer(thisPlayer):
    if thisPlayer=='O':
        thisPlayer = 'X'
    else:
        thisPlayer = 'O'
    return thisPlayer
   

main()

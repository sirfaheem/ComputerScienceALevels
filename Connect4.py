BLANK = '.'
board = [[BLANK for col in range(7)] for row in range(6)]

def main():
    initBoard() #initializeBoard
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

def checkHorizontalLine(board, thisPlayer, row, winnerFound):
    for col in range(4):
        if board[row][col] == thisPlayer and \
           board[row][col+1] == thisPlayer and \
           board[row][col+2] == thisPlayer and \
           board[row][col+3] == thisPlayer:
            winnerFound=True
    return winnerFound

def checkVerticalLine(board, thisPlayer, col, winnerFound):
    for row in range(4):
        if board[row][col]== thisPlayer and \
           board[row+1][col]== thisPlayer and \
           board[row+2][col]== thisPlayer and \
           board[row+3][col]== thisPlayer:
            winnerFound=True
    return winnerFound

def checkDiagnol(board, thisPlayer, row, col, winnerFound):
    if board[row+1][col+1]== thisPlayer and \
           board[row+2][col+2]== thisPlayer and \
           board[row+3][col+3]== thisPlayer:
            winnerFound=True

    if board[row-1][col-1]== thisPlayer and \
           board[row-2][col-2]== thisPlayer and \
           board[row-3][col-3]== thisPlayer:
            winnerFound=True

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
    for row in range(6):
        for col in range(7):
            board[row][col]=BLANK
def setup():
    #global gameEnd
    thisPlayer = 'O'
    gameEnd=False
    return thisPlayer, gameEnd

def outputBoard():
    for heading in range(7):
        print( heading, end='\t')
    print()
    for row in range(5,-1,-1):
        for col in range(7):
            print( board[row][col], end='\t')
        print()
        print()

def playerMakesMove(board, thisPlayer):
    validCol = playerChoosesCol(board, thisPlayer)
    validRow = findFreeRow(board, thisPlayer, validCol)
    board[validRow][validCol] = thisPlayer
    return validRow, validCol

def playerChoosesCol(board, thisPlayer):
    print(thisPlayer+"'s Turn: ")
    thisCol = int(input('Enter a column No: '))
    while not columnNumberValid(board, thisCol):
        thisCol=int(input('Enter a valid column No: '))
    return thisCol

def columnNumberValid(board, colNum):
    valid = False
    if colNum>=0 and colNum<7:
        if board[5][colNum]==BLANK:
            valid = True
    return valid

def findFreeRow(board, thisPlayer, validCol):
    thisRow = 0
    while board[thisRow][validCol] != BLANK:
        thisRow+=1
    return thisRow

            
def swapPlayer(thisPlayer):
    if thisPlayer=='O':
        thisPlayer = 'X'
    else:
        thisPlayer = 'O'
    return thisPlayer
   

main()

def main():
    while 1:
        print('faheem')
def a():
    initializeBoard()
    setUpGame()
    outputBoard()

    while gameFinished == False:
        playerMakesMove()
        outputBoard()
        checkGameFinished()
        if gameFinished == False:
            swapPlayer()

main()

        

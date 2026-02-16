userInput = input('Enter text to save to file: \n')
FileRef = open ('TestFile.txt', 'w')
FileRef.write(userInput)
FileRef.close()



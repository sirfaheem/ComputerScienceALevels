import os

filePath = '/Desktop/untitled.png'
print(filePath)

if os.path.isfile(filePath):
    os.remove(filePath)
    print('File has successfully been deleted!')
else:
    print('This file does NOT exist !!!')

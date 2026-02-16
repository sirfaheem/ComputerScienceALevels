def findPal(word):
    #iterative solution
    pal = True
    print(len(word))
    for x in range(len(word)//2):
        print(x)
        print(x-len(word))
        print(word[x], end = ' ')
        print(word[len(word)-x])
        #if word[x]!= word[len(word)-x+1]:
            #pal= False
    return pal
print(findPal('abba'))
print(findPal('abbu'))


    #recurcive solution

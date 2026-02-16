def findPal(word):
    #iterative solution
    pal = True
    mid=len(word)//2
    for x in range(mid):
        if word[x]!= word[-(x+1)]:
            pal= False
    return pal
print(findPal('abba'))
print(findPal('ababa'))
print(findPal('abbu'))



def findPal(word):
    #iterative solution
    pal = True
    mid=len(word)//2
    for x in range(len(word)//2):
        if word[mid+x]!= word[mid-x]:
            pal= False
    return pal
print(findPal('abba'))
#print(findPal('ababa'))
#print(findPal('abbu'))



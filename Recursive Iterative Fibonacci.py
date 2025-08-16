
def fibRecursive(n):
    if n==1:
        return 1
    else:
        return n+fibRecursive(n-1)
    
def fibIterative(n):
    total = 0
    for x in range (1,n+1):
        total +=x
    return total

print(fibIterative(7))
print(fibRecursive(7))


def fibRecursive(n:int):
    if n == 0:
        return 0
    else:
        return n + fibRecursive(n - 1)


def fibIterative(n:int):
    total = 0
    for x in range(1, n + 1):
        total += x
    return total


print(fibIterative(7))
print(fibRecursive(7))

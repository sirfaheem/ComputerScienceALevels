import random
myList = [random.randint(1, 20) for x in range(30)]
myList.sort()

def BinarySearch(item, lBound, uBound, myList):
    # base case
    if uBound < lBound:
        return -1

    index = (uBound + lBound) // 2
    ThisItem = myList[index]

    if item == ThisItem:
        return index
    elif item > ThisItem:
        return BinarySearch(item, index + 1, uBound, myList)
    else:
        return BinarySearch(item, lBound, index - 1, myList)

def main():
    print(myList)
    item = int(input('Enter item to search: '))
    found = BinarySearch(item, 0, len(myList)-1, myList)
    if found != -1:
        print(f'{item} found at index {found}')
    else:
        print(f'{item} not found in the list')

main()


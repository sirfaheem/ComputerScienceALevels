import random
myList = [random.randint(1, 50) for x in range(20)]
myList.sort()

def BinarySearch(item, lBound, uBound, myList):
    # base case item not found in the list
    if uBound < lBound:
        return -1 #item not in the list

    index = (uBound + lBound) // 2
    ThisItem = myList[index]

    if item == ThisItem: #base case 2 item found
        return index
    elif item > ThisItem: #general case
        return BinarySearch(item, index + 1, uBound, myList)
    else: #general case 2
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


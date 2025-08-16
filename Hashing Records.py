class Customer:
    CustomerID = 0
    CName = ""
    Contact = ""
    isActive = False

MaxIndex = 9
CustomerArray = [Customer for x in range(MaxIndex+1)] #RECORD

def Hash(Key):
    global MaxIndex
    global CustomerArray
    Address = Key % (MaxIndex+1)
    return Address


def Insert(NewRecord):
    global CustomerArray
    Index = Hash(NewRecord.CustomerID)
    while CustomerArray[Index].CustomerID!=0:
        Index +=1
        if Index>MaxIndex:
            Index = 0
    CustomerArray.insert(Index,NewRecord)

def Search(ThisID):
    Index = Hash(ThisID)
    while CustomerArray[Index].CustomerID != ThisID and CustomerArray[Index].CustomerID !=0:
        Index+=1
        if Index >MaxIndex: Index = 0
    if CustomerArray[Index].CustomerID!=0:
        return CustomerArray[Index]
    else:
        return -1
    

ThisID = int (input ("Enter customer ID [0 to exit]: "))

while ThisID != 0:
    newRecord = Customer()
    newRecord.CustomerID = ThisID
    newRecord.CName = input("Enter Customer name:")
    Insert(newRecord)
    ThisID = int (input ("Enter customer ID [0 to exit]: "))

#print(Search(int(input("Enter ID: "))))
for x in range(MaxIndex):
    print(CustomerArray[x].CustomerID,CustomerArray[x].CName) 

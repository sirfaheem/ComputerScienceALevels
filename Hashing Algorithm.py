




MaxIndex = 9
CustomerIDs = [0] * (MaxIndex+1) #INTEGER

def Hash(Key):
    global MaxIndex
    Address = Key % (MaxIndex+1)
    return Address


def Insert(NewRecord):
    global CustomerIDs
    Index = Hash(NewRecord)
    while CustomerIDs[Index]!=0:
        Index +=1
        if Index>MaxIndex:
            Index = 0
    CustomerIDs[Index] = NewRecord

def Search(ThisID):
    Index = Hash(ThisID)
    while CustomerIDs[Index] != ThisID and CustomerIDs[Index] !=0:
        Index+=1
        if Index >MaxIndex: Index = 0
    if CustomerIDs[Index]!=0:
        return CustomerIDs[Index]
    else:
        return -1
    

ThisID = int (input ("Enter customer ID [0 to exit]: "))
       
while ThisID != 0:
    Insert(ThisID)
    ThisID = int (input ("Enter customer ID [0 to exit]: "))

print(CustomerIDs)
print(Search(int(input())))
print(Search(int(input())))

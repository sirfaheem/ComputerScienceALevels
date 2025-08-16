SIZE = 10
class SRec:
    ID = -1
    name = ""
    age = 0
    gpa = 0.0
HashTable = []
for x in range(SIZE):
    HashTable.append(SRec)

def Hash(Key):
    Address = Key % (SIZE)
    return Address

def Insert(aRec):
    Index = Hash(aRec.ID)
    print(HashTable[Index].ID)
    try:
        while HashTable[Index].ID != -1:
            Index +=1
            if Index>SIZE:
                Index = 0
        HashTable.insert(Index, aRec)
    except IndexError :
        print(Index)

def FindRecord(SearchKey):
    Index = Hash(SearchKey)
    try:
        while (HashTable[Index].ID != SearchKey)and HashTable[Index].ID != -1:
           Index +=1
           if Index >SIZE: Index =0
        if HashTable[Index].ID !=-1:
           return HashTable[Index]
        else: return SRec
    except IndexError:
        print(Index)


mRec = SRec

mRec.ID = 487573
mRec.name = "faheem"
mRec.age = 34
mRec.gpa = 3.7

Insert(mRec)
mRec.ID = 852121
mRec.name = "ali"
mRec.age = 36
mRec.gpa = 3.8
Insert(mRec)

for x in range(SIZE):
    print(HashTable[x].ID, HashTable[x].name)

foundObject = FindRecord(487573)
if foundObject.ID !=-1:
    print(foundObject.ID)
    print(foundObject.name)
    print(foundObject.age)
    print(foundObject.gpa)

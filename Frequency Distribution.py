def main():
    FArray = [0] *26
    AlphaArray = [chr(x+65) for x in range(26)]
    #print(AlphaArray)
    fname = "SNames.txt"
    Freq(FArray,fname)
    #print(ord('A'))
    for x in range (26):
        print(AlphaArray[x], end="\t")
        print(FArray[x])
    bubbleSort(FArray, AlphaArray)
    print()
    print("High to low frequency")
    for x in range (26):
        print(AlphaArray[x], end="\t")
        print(FArray[x])
    print(highFreq(FArray))
def Freq(arr, fname):
    with open(fname,"r") as f:
        myText = f.read()
        myText = myText.upper()
        
        for x in range(len(myText)):
            ThisChar = myText[x:x+1]
            Index = ord(ThisChar)
            Index -= 65
            if Index >=0 and Index <26:
                arr[Index]+=1
            #print(ord(ThisChar)-65, end=' ')

def highFreq(arr):
    maxF = -1
    for x in range(len(arr)):
        if arr[x]>maxF:
            maxF=arr[x]
            ThisChar = x
    ThisChar = chr(ThisChar+65)
    return ThisChar

def bubbleSort(arr,arr2):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1):
            if arr[j]<arr[j+1]:
                arr[j],arr[j+1] = arr[j+1], arr[j]
                arr2[j],arr2[j+1] = arr2[j+1], arr2[j]
                




                
main()

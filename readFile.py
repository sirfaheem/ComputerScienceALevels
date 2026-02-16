Temp=''

with open("CData.txt", "r") as f:
    Temp = f.readline().strip()
    while len(Temp)>0:
        print(Temp)
        Temp = f.readline().strip()

hnum=str(input("enter hexa to convert to denary"))
dnum=0
c=0
cb=len(hnum)-1
def convh(hnum):
    global dnum
    global cb
    global c
    f=False
    if "a"<=hnum[c]<="f" or "A"<=hnum[c]<="F":
        if hnum[c]=="a" or "A":
            dnum=dnum+10*16**cb
            f=True
        elif hnum[c]=="b" or "B":
            dnum=dnum+11*16**cb
            f=True
        elif hnum[c]=="c" or "C":
            dnum=dnum+12*16**cb
            f=True
        elif hnum[c]=="d" or "D":
            dnum=dnum+13*16**cb
            f=True
        elif hnum[c]=="e" or "E":
            dnum=dnum+14*16**cb
            f=True
        elif hnum[c]=="f" or "F":
            dnum=dnum+15*16**cb
            f=True
    if"0"<=hnum[c]<="9":
        dnum=dnum+int(hnum[c])*16**cb
        f=True
    if f:
        c+=1
        cb-=1
    if c<(len(hnum)) and cb!=-1:
        convh(hnum)
    return dnum
        
print(convh(hnum))

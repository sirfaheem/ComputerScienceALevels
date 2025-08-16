import time
import sys
import os
##def countDown(n):
##    for x in range (n, -1, -1):
##        print(x)


def countDown(n):
    if n !=-1:
        #print(n, end='\r',flush=True)
        sys.stdout.write(str(n))
        sys.stdout.flush()
        #os.system('cls')
        #os.system('clear')
        time.sleep(1)
        countDown(n-1)
countDown(7)

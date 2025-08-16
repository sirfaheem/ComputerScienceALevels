import datetime

numArray = [0] * 100
Num2DArray = [[0 for col in range(5)] for row in range(10)]
DateArray = [None] * 10

DateArray[0] = datetime.datetime.today()
DateArray[1] = datetime.datetime(1998, 4,23)
DateArray[2] = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
DateArray[3] = datetime.datetime.now(datetime.UTC)
DateArray[4] = datetime.datetime.today()
print(DateArray[3])
print(DateArray[2])

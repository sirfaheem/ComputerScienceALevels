class CityTemp:
    cityName = ''     #string
    temperature = 0.0 #float

myData = [CityTemp() for i in range(3)]


for x in range (3):
    myData[x].cityName = "none"
    myData[x].temperature = -2.5

myData[1].cityName = "New York"

for x in range (3):
    print(myData[x].cityName)
    print(myData[x].temperature)

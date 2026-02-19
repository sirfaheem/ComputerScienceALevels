import pickle


class CarRecord:
    def __init__(self):
        self.VehicleID = ""
        self.Registration = ""
        self.DateOfRegistration = None
        self.EngineSize = 0
        self.PurchaseSize = 0.00


Car = [CarRecord()] * 10  # Create an empty array of 10 objects called Car

for i in range(10):
    ThisCar = CarRecord()  # Create an instance of class CarRecord named ThisCar
    Car[i] = ThisCar  # Assign reference of this Car object to array location

Car[1].EngineSize = 2500
Car[5].EngineSize = 3000

print(Car[1].EngineSize)
print(Car[5].EngineSize)
print("\n \n")

for i in range(10):
    print(Car[i].EngineSize)

print("\n \n")

CarFile = open('Cars.DAT', 'wb')

for i in range(10):
    pickle.dump(Car[i], CarFile)

CarFile.close()

Car[1].EngineSize = 3500
Car[5].EngineSize = 8000

Car2 = [CarRecord()] * 10
#for i in range(10):
#ThisCar = CarRecord()
#Car2[i] = ThisCar

CarFile = open('Cars.DAT', 'rb')

while True:
    try:
        Car2.append(pickle.load(CarFile))
    except EOFError:
        break

CarFile.close()

print("\n")
for i in range(10):
    print(Car2[i].EngineSize)
    print("")

#print(Car[1].EngineSize)
#print(Car[5].EngineSize)

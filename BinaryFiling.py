import pickle
import datetime

class CarRecord:
    def __init__(self):
        self.VehicleID = ""
        self.Registration = ''
        self.RegistrationDate = None
        self.EngineSize = 0
        self.PurchasePrice = 0.0

Car = [CarRecord() for i in range(4)]
CarFile = open('CarFile.BIN', 'wb')
for i in range(4):
    pickle.dump(Car[i], CarFile)
CarFile.close()

CarFile = open('CarFile.BIN', 'rb')
Car = []
while True:
    Car.append(pickle.load(CarFile))
    
CarFile.close()

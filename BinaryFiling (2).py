import pickle
import datetime

class CarRecord:
    def __init__(self):
        self.VehicleID = ""
        self.Registration = ''
        self.RegistrationDate = None
        self.EngineSize = 0
        self.PurchasePrice = 0.0
    def prn(self):
        print(self.Registration,self.EngineSize,self.PurchasePrice)

Car = [CarRecord() for i in range(4)]
Car[0].Registration = 'LXV 2342'
Car[0].prn()
def ReadFile:
    CarFile = open('CarFile.BIN', 'rb') read
    Car = []
    while True:
        Car.append(pickle.load(CarFile))
        
    CarFile.close()


CarFile = open('CarFile.BIN', 'ab+') append
CarFile = open('CarFile.BIN', 'wb') write
for i in range(4):
    pickle.dump(Car[i], CarFile)
CarFile.close()


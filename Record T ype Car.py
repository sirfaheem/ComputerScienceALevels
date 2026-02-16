class CarRecord:
    VehicleID = ""
    Registration = ""
    EngineSize = 0
    PurchasePrice = 0.0


ThisCar = CarRecord
ThisCar.VehicleID = "LZX 3464"
ThisCar.EngineSize = 1800
ThisCar.PurchasePrice = 26000

print(ThisCar.VehicleID)
print(ThisCar.PurchasePrice)
print(ThisCar.EngineSize)

class Vehicle:
    licenseCode = ""
    serialCode = ""
    def turnOnAirConditioner(self):
        print("Turn on : Air")

class Car(Vehicle):
    def sayHello(self):
        print("Hello World")

class PickUp(Vehicle):
    colorPickup = ""
    def colorPickUpp(self):
        print("รถสี :",self.colorPickup)

class Van(Vehicle):
    pass

class EstateCar(Vehicle):
    pass

car1 = Car()
car1.turnOnAirConditioner()
car1.sayHello()

pickUp1 = PickUp()
pickUp1.turnOnAirConditioner()
pickUp1.colorPickup = "red"
pickUp1.colorPickUpp()

van1 = Van()
van1.turnOnAirConditioner()

estateCar1 = EstateCar()
estateCar1.turnOnAirConditioner()
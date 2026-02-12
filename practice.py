class Vehicle:
    def __init__(self,speed):
        self.speed = speed
    def displaydetails(self):
        print(self.speed)

class Car(Vehicle):
    def __init__(self,speed,mileage):
        super().__init__(speed)
        self.mileage = mileage
    def display(self):
        super().displaydetails()
        print(self.mileage)

class Smartcar(Car):
    def __init__(self,speed,mileage,engine):
        super().__init__(speed,mileage)
        self.engine = engine
    def dis(self):
        super().display() #Function overriding--refers to the polymorphism concept that executes the functions of child class only when the function name is same in both parent and child
        print(self.engine)

obj1 = Smartcar(50,10,"engine")
obj1.dis()
# a = input("Enter the speed:")
# b = input("Enter the mileage:")
# c = input("Enter the engine type:")
# obj2 = Smartcar(a,b,c)
# obj2.displaydetails()
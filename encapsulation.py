class Vehicle:
    def __init__(self, speed, engine):
        self.speed = speed  # public access modifier is the default modifier
        self._engine = engine # protected access modifier (underscore is used for protected variables)
        self.__price = 3000 # private access modifier( double underscore is used for private access modifier)
    def get_price(self):
        return self.__price
    def set_price(self,price):
        self.__price = price
obj1 = Vehicle(30,"engine")
obj1.set_price(200)
print(obj1.get_price())



from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass
class UPI(Payment):
    def pay(self):
        print("Payment can be done using UPI")
obj = UPI()
obj.pay()

class Product:
    def prod(self, *args):
        s = args[0]
        for i in args[1:]:
            s *= i
        return s

obj = Product()
print(obj.prod(4,7,8))



from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def display(self):
        pass

class Dog(Animal):
    def display(self):
        print("Hi doggy")
obj1 = Dog()
obj1.display()

class ATM(ABC):
    @abstractmethod
    def display(self):
        pass
class Withdraw(ATM):
    def display(self):
        total = 2000
        balance = total - 500
class Checkbalance(ATM):
    def display(self):
        total = 2000
        balance = total - 500
        print(balance)



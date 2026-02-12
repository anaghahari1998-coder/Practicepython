class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(self.name)
        print(self.age)

obj = Student("Ann", 15)
obj.display()



class Book:
    def __init__(self, text):
        self.text = text
    def display(self):
        print(self.text)

obj1 = Book("Notebook")
obj1.display()

obj2 = Book("Graphbook")
obj2.display()



class Person:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def show(self):
        print(self.name)
        print(self.country)

p1 = Person("Rohan", "Dubai")
p1.show()
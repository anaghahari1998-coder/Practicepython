class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display_info(self):
        print(self.name)
        print(self.age)
class Male(Person):
    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.salary = salary
    def display_info(self):
        # super().display_info()
        print(self.salary)

obj = Male("Sachin",25,45000)
obj.display_info()
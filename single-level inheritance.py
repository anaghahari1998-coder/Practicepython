class Animal:  #Animal is the parent class
    def __init__(self,text):
        self.text = text
    def name(self):
        print(self.text)
class Tiger(Animal):  # this is single level inheritance, Tiger is the child class
    def word(self):
        print("Hi")
        super().name()  # super() is the keyword used to denote the properties of a parent class
obj = Tiger("helloooo")
obj.word()
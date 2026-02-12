class Fruits:
    def display(self, name=None):
        if name:
            print("Hello " + name)
        else:
            print("Good morning")
obj1 = Fruits()
obj1.display()
obj1.display("Orange")
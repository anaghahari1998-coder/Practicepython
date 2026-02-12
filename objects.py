class Demo:
    x = "ABC School" # it's a property of a class, x is the global variable/class variable
    def __init__(self,name): # self is used to distinguish between each objects that's been created, __init is a constructor
        print("this is a constructor")
        self.name = name # self.name is a variable which is used to distinguish between current and other object's name property, name is a local variable/instance variable
    def display(self):
        print(self.name)
        print(Demo.x)
demo1 = Demo("Hello")
demo1.display()

# demo2 = Demo("Hey")
# demo2.display()
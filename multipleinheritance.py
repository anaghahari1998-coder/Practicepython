class Father:
    def skills(self):
        print("Father's skills:Singing,Art")
class Mother:
    def skills(self):
        print("Mother's skill:Cooking")
class Child(Father, Mother):
    def skills(self):
        super().skills()
        print("Child's skill")
ch_obj = Child()
ch_obj.skills()

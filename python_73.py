# multiple inheritance in python

# multiple inheritance is a powerful feature in oop that allows a class to inherit attribute and methods from multiple parents classes.
# this can be useful in s=ituations where a class needs to inherit functionality from multiple sources.

# syntax:
# class childclass(parentclass1,parentclass2,parentclass3):


class employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"the name is{self.name}")


class dancer:
    def __init__(self, dance):
        self.dance = dance

    def show(self):
        print(f"the dance is{self.dance}")


class danceremployee(employee, dancer):
    def __init__(self, dancer, name):
        self.dance = dancer
        self.name = name
        
o = danceremployee("mass","rohit")
print(o.name)
print(o.dance)
o.show()
print(danceremployee.mro())
# mro - method resolution order

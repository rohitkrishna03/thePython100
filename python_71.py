# single inheritance:

# single inheritance is a type of inheritance where a class inherits properties and behavior from a single parentclass.
# this is the simplest and most common form od inheritance.

# syntax:
# the syntac for single inheritance in python is staraightforword and easy to understand.
# to create a new class that inherits from a parent class, simply specify the parent class in the class definition, inside the parentheses
# class
# childclass(parentclass):
    #    class body
    
    
class animal:
    def __init__(self, name, species):
        self.name=name
        self.species=species
        
    def make_sound(self):
        print("sound made ny the animal")
        
class dog(animal):
    def __init__(self, name, breed):
        animal.__init__(self,name, species="dog")
        # the above in animal.__init__ which is called super class where we used the overriding method.
        self.breed=breed
        
    def make_sound(self):
            print("barks!")
d= dog("dog","doggerman")
d.make_sound()
a= animal("dog","doggerman")
a.make_sound()
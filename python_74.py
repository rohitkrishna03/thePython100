# multilevel inheritance
# multilevel inheritance in python
# the multilevel inheritance is a type of inheritance in object-oriented programming
# where a derived class inheritance from another derived class.
# this type of inheritance allows you to build a hirerachynof class where one class builds upon another
# leading to more specialized class.

# in python , multilevel inheritance is achieved using the class hierrachy. the syntax for multilevel inheritance 
# is quite simple and follow the same syntax as single inheritance.


class animal:
    def __init__(self,name, species):
        self.name=name
        self.species=species
        
    def show_details(self):
        print(f"name: {self.name}")
        print(f"species {self.species}")
        
class dog(animal):
    def __init__(self, name, breed):
        animal.__init__(self,name, species="dog")
        self.breed=breed
        
    def show_details(self):
        animal.show_details(self)
        print(f"breed: {self.breed}")
class goldenretriver(dog):
    def __init__(self, name, color):
        dog.__init__(self,name, breed="goldenretriver")
        self.color=color
        
    def show_details(self):
        dog.show_details(self)
        print(f"color:{self.color}")
o = goldenretriver("jimmy","grey") 
o.show_details()

# if you want to see from where it is fetching the details 
# go with print(goldenretriver.mro())
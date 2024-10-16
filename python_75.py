# hybrid inheritance in python 
# hybrid inheritance is a combination of multiole inheritance and single inheritancein oops
# it is a type of inheritance in which multiple inheritance is used to inherit the properties of multiple base classes into a single derived class,
# and single ingheritance is used to inherit the properties of the derived class into a sub-derived class.

# in python, hybrid inheritance can be implemented by creating a class hierarchy, in which a base class is inherited by multiple derived classes,
# and one of the derived classes in further inherited by a sub-derived class.

# the basic syntax of hybrid inheritance is 

# this is the syntax of the hybrid inheritance``
class baseclass:
    pass
class derived1(baseclass):
    pass

class derived2(baseclass):
    pass

class derived3(derived1, derived2):
    pass






# hierarchical inheritance
# hierarchical inheritance is a type if inheritance in oop where multiple subclasses inherit from a single base class.
# in other words, a single base class as a parent class for multile subclasses.
# this is a way of establishing relationships between classes ina hierarchical manner.
class baseclass:
    pass
class d1(baseclass):
    pass
class d2(baseclass):
    pass

class d3(d1):
    pass

class d4(d2):
    pass

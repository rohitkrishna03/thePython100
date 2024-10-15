# method overriding in python
# method overriding is a powerful feature in object-oriented programming language that allows you to redefine a method in a derived/child class.
# the method in the derived class is said to override the method in the base class.
# when you create an instance of the derived class and call the overridden method.
# the version of the method in the derived class is executed, rather than the version in the base class.
#  In other words, the subclass "overrides" the method of the parent class, allowing the subclass to have its own version of the method.
class shape:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def area(self):
        return self.x*self.y
    
class circle(shape):
    def __init__(self, radius):
        self.radius =radius
        super().__init__(radius, radius)
    # here we use the super to access the parent class method.
        
    def area(self):
        return 3.14 * super().area()
# rec = shape(3, 5)
# print(rec.area())
        
cir =circle(2)
print(cir.area())
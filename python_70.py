# method overloading in python:
# operator overloading is a future that allows developers to redefine the behavior of mathematical amd comparision operator
# for custom data types. this means that you can use the standard mathametical operators(+,-,*,/)and comparision operators(<,>,==,etc)in your oen classes, just 
# as you would for built-in data types int, float, double.

# why do we need operator overloading?
# operator overloading allows you to create more readable and intuitive code.
# for example, consider a custom class that represents a class in a 2d space.
# you could define a method called "add" to add points together, but using the + operator makes the code more concise adn readable.
# Operator overloading is a feature in Python that allows you to define custom behavior for standard operators like +, -, *, /, etc.,
# when applied to instances of your class. This is done by overriding special methods in your class, also known as magic methods or dunder methods
# (because they start and end with double underscores, like __add__ for +, __sub__ for -, and so on).
# p1=point(1,2)
# p2=point(3,4)
# p3=p1+p2
# print(p3.x, p3.y)
class vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k
        
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    
    def __add__(self,x):
        return f"{self.i +x.i}i +{self.j +x.j}j +{self.k +x.k}k"
v1 = vector(3, 5, 6)
print(v1)
v2 = vector(1,2,3)
print(v2)
print("below is the sum of vectors")
v3 = v1+v2
print(type(v3))
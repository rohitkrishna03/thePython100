# magic and dunder(double underscore) method
# these are special methods that you can define in your classes and when invoked, they give you a powerful way to manipulate objects and their behaviour.
# 
# magic methods also known as "dunder" from the double underscore surroundinf their names are powerful tools that allows you to customize
# the behavior of your classes. they are used to implement special methods such as the addition subtraction and comparision operator, as well as some more advanced techniques like description and properties.
# lets take a look of some of the most commonly used magical methods in python.
# 
# the __init__ method is the specia method that is automatically involved when you create a mew isntance of a class.
# this method is  responsible for setting up the objects initial state, and it is where you would typically define any instance variable that you need. 
# also called "constructor", in file python_66.py

# this is using the __len__ method
# class employee:
#     name= "rohit"
#     def __len__(self):
#         i=0
#         for c in self.name:
#             i =i+1
#         return i
    
# e = employee()
# print(e.name)
# print(len(e))
            
            
# this is using the __init__ method

class employee:
    def __init__(self, name):
        self.name=name
    def __len__(self):
        i =0
        for c in self.name:
           i = i +1
        return i 
    def __str__(self):
        return f"the name of the employee is {self.name}"
    
# in another file just write to se this output

# from emp import employee
# e=employee("rohit")
# print(e)
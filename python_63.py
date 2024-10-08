# python class
# in python, class are a way to define custom data types that can store data and define function that can manipulate that data
# one type of function that can be defined within a class is called a method.

# what are python class methods?

# a class method is a type of method that is binds to the class and nt the instance of the class.
# in other words, it operates on the class as a whole, rather than a specific instance of @classmethod decorator, followed by the function definition.
# the first argument if the function is always "cls", which represents the class itself.

# why use python class method?
# class method are useful in several situations, for example you might want ti create a factory method that creates instance of your class in a specific way.
# you could define a class method that creates the instance and return it to the caller.

# another common use case is to provide alternate constructor for your class.
# this can be useful if you want to create instance of your class in multiple ways, but still have a constant interface for doing of
# 

class employee:
    company = "apple"
    def show(self):
        print(f"the name is {self.name} and company is {self.company}")
        
        
    @classmethod
    def changecompany(cls, newcompany):
      cls.company =newcompany
        
e1 = employee()
e1.name = "harry"
e1.show()
e1.changecompany("tesla")
e1.show()
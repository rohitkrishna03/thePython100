# constructor in python

# a constructor is a special method in a class used to create and initialize an object of a class.
# there are different types of constructors
# constructor is automatically created when an object of a class is created.

# a constructor is a unique function that gets called automatically when an object is create dof class.
# the main purpose of a constructor is to initialize values to the data members of class.add(
# it cannot return any other value other than none.

# syntax:
# def __init__(self):
# initialization

class person:
    def __init__(self,n,o):
       print("hey i am a person")
       self.name=n
       self.occ=o
       
    
    def info(self):
        print(f"{self.name} is a {self.occ}")
              
a= person("rohit","dev")
b= person("krishna","game")
a.info()
b.info()

# here every time we create am object it is calling the constructor method/
    
    
# dir(), __dict__ and help() method in python 
# we must look into dir(), __dict__() and help() attributes/methods in python.
# they make easy for us to understand how class resolve various functions and execute code.
# in python, there are three built in functions that are commonly used to get information about object like dir,dict and help.

# the dir() method:
# dir():
# the dir function returns alist of all the attributes and methods(including dunder method) avaliable for an object.it is a useful tool for discovering what you can do with an object.

# x =[1,2,3]
# dir(x)

class person:
    def __init__(self, name,age):
        self.name=name
        self.age=age
        self.version=1
p =person("rohit", 25)
print(p.__dict__)
print(help(person))
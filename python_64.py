# class method as alternate constructor
# in object-oriented programming , the term "constructor" refers to a special type of method tha is automatically executed when an object is created from a class.
# the purpose of a constructor is to initialize the object attribute,allowing the object to be fully functional and ready to use.
# 
# however, there are times when you may want to create an object in a different way, or with different initial value, than what is provided by the default constructor.
# this is where class method can be used as alternative constructor.

#  a class method belongs to the class rather than to a instance of the class. one common use case for the class method as alternative constructor is
# when you want to create an objective from data that is stored in a different format,
# such as a string or a object.For example, consider a class named "person" that has two attributes "name" and "age"
# the default constructor looks like: 

class employee:
    def __init__(self, name, salary):
        self.name=name
        self.salary = salary
        
    @classmethod
    def fromStr(cls, string):
        return cls(string.split("-")[0], string.split("-")[1])
e1 = employee("rohit",20000)
print(e1.name)
print(e1.salary)

string ="john-20000"
e2 = employee.fromStr(string)
print(e2.name)
print(e2.salary)

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    @classmethod
    def from_string(cls, string):
        name,age = string.split(',')
        return cls(name, int(age))
    
    
person = Person.from_string("john doe, 30")
print(person.name, person.age)
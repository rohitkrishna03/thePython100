# getters and setters are method are used to access the values of an objects properties.
# they are used to return teh value of a specific property.
# and are typically defined using the @property decorator.
#here is the synatx examle for getters and setters

# class myclass:
#     def __init__(self, value):
        
#         self._value=value
#     @property
#     def value(self):
#         return self._value
# creating methods which behaves like property
# in the below example we will create ten_value which is method and can act like property.
# class myclass:
#     def __init__(self, value):
#         self._value = value
        
#     def show(self):
#         print(f"value is {self._value}")
            
#     @property
#     def ten_value(self):
#         return 10* self._value
        
#     @ten_value.setter
#     def ten_value(self, new_value):
#         self._value = new_value/10
        
# obj = myclass(10)
# obj.ten_value =67
# print(obj.ten_value)
# obj.show()

# using the normal function to achieve getter and setter behavior()


# class home:
#     def __init__(self, age=0):
#         self._age = age
#     def get_age(self):
#         return self._age
#     def set_age(self, a):
#         self._age =a
      
# rohit = home()        

# rohit.set_age(25)
# print(rohit.get_age())
# print(rohit._age)

# here we sue the property function  to achieve getter and setter behavior

class homee:
    def __init__(self):
        self._age=0
        # using the get function
    def get_age(self):
        print("getter method")
        return self._age
    # using the set function
    def set_age(self,y):
        print("setter method")
        self._age = y 
        # using the del function
    def del_age(self):
            del self._age
    age = property(get_age,set_age,del_age)
        
rohit =homee
        
rohit.age =25
print(rohit.age) 
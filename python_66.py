# super keyword in python

# the super() keyword is used to refer the parent class.
# it is especially useful when a class inherit from multiple parent classes and you want to call a method from on eof the parent class.

# when a class inherits from a parent class, it can override or evaluate or exntnf the methods defined in the parent class.
# however, sometimes you might want to use the parent class method in the child class.
# this is where the super() keyword comes in handy.
# class parentclass:
#     def parent_method(self):
#         print("this is parent method.")

# class childclass(parentclass):
#     def parent_method(self):
#         print("rohit")
#     def child_method(self):
#         print("this is child class")
#         super().parent_method()
        
# child_object = childclass()
# child_object.child_method()
# # the above is the base usage of the super keyword()

# now lets see the real attempt of this.

class employee:
    def __init__(self, name, id):
        self.name=name
        self.id=id
        
class programmer(employee):
    def __init__(self, name, id, lang):
        super().__init__(name, id)
        self.lang=lang
        
rohit = employee("rohit", "123")
krishna = programmer("harry", "456","python")
print(rohit.name)
print(rohit.id)
print(krishna.lang)
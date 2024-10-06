# access specifiers/modifiers
# access  specifiers or access modifiers in python programming are used to limit the access of calss variable and class method outside of class while implementing concepts in inheritance.
# types of access specifiers/modifiers:
# public access modifiers
# private access modifiers
# protected access modifiers.

# public access modifiers:
# all the variabkes and methods(member function) in oython are default public.
# any instance variable in a class followed by the "self" keyword.
# that is self.var_name are public accessed.
class students:
    def __init__(self, age, name):
        self.age=age
        self.name=name
        
obj = students(21,"rohit")
print(obj.age)
print(obj.name)



# private access modifiers
# by definition, private member if class (variable or method) are those members which are only accessible inside the class.
# we cannot use private members outside of class
# in python, there is no strict concept of private access modigiers linke in other programming languages.
# however a convention has been estlabished to indicate that a variable or method should has been estlabished to indicate the variable or method should be considered private
# by prefexing its name with a doubke underscore(__)
# this is known as a weak internal use indicator and its convention only, not a strict rule.
# code outside the class still access these private variables and methods, but it is generally understood hat they should not be accesses=d or modified.
#
class employee:
    def __init__(self):
        self.__name = "rohit"
        
a = employee()

print(a.__name) #cannot be accessed directly

print(a._employee__name) #can be accessed indirectly


# name manglig in python techinque is a technique used to protected class -private and superclass-private attribute from being accidently overwritten by subclass. names of clas private and superclass and superclass private attribute
# are transformed by the addition of a single addition of a single leading underscore an ddouble underscore leading underscore respectively.add(
#  
#  protected access modifier 
# in object- oriented programming anguage(oop), the term :protected is used to describe a member (i.e, method or attribute)
# of a class that us intented to be accessed only by the class itself and ots subclass. 
# in python, the convertion for indicating that a underscore(_). for example, if a class has a method called
# _my_method, it is indicating that the method should only be accessed by the class itself and its subclass.

























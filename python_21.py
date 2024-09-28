# docstring in python

# python docstring are the string literals that appear right after the definition 
# of a function, method, class or module.
def square(n):
    '''take a number n, return the square of n'''
    print(n**2)
square(5)
print(square.__doc__)
# whenever string literals are present just after the definition of a sfunction, mudule
# class or method, they are associated with object and their doc attributes.
# and (we can later) use this attribute to retrieve this docstring


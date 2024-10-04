# python decorators
# python decorators are a powerful and versatile tool that allows you to modufy the behavior of function and method.
# they are a way to extend a function oe method without modifing its source code.
# A decorator is a function that takes another fynction as an argument and return a new functionthat modifies the behavior of orginal function.
# the new function is often reffered as decorator function.

# the basic suntax of the decorator function:
# @decorator_function
# def my_function():
#     pass

# def great(fx):
#     def mfx():
#         print("good morning")
#         fx()
#         print("thats for using this greet function")
#         return mfx
# def hello():
#     print("hello world!")    
# hello()
# here if we run this program it will only show the output as helloworld and here if we want to use the great also how is that possible . yes it ispossible with @decorator method
# def great(fx):
#     def mfx():
#         print("good morning")
#         fx()
#         print("thats for using this greet function")
#     return mfx
# @great
# def hello():
#    print("hello world!")    
   
# def add(a,b):
#     print(a+b)
# hello()
# great(add)(1,2)  # this line shows issues
# if we add like this with out defining args and kwargs in function this will pull out errors
# here we will rewrite the program again
def great(fx):
    def mfx(*args,**kwargs):
        print("good morning")
        fx(*args, **kwargs)
        print("thanks for using the greet function")
        return mfx

def hello( ):
    print("hello world!")
@great        
def add(a, b):
    print(a+b)
hello( )
add(1,2)
# great(add)(1, 2)
        
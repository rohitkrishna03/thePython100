# lambda function in python 
# lambda function is a small anonymous function without a name.
# it is defined s=using keyword and has the following syntax.

# lambda function are often used in situations where a small function is required for a short period of time.
# they are commonly used as arguments to high-order function, such as map, filter and reduce argument to higher-order function such as map, filter and reduce.

# def double(x):
#     return x*2

double = lambda x: x*2
cube = lambda x: x*x*x
average = lambda x ,y, z: (x+y+z)/3
print(double(5))
print(cube(5))
print(average(3,4,5))

# lilewise of we write the multiple function as
 
def multiple(x, y):
 return x* y
print(multiple(3,4))


# but in lambda we write as 

multiple = lambda x, y: x*y
print(multiple(3,5))
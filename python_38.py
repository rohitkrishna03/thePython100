# local and global variable
# a variable is a named location in memory that stores a value.
# in python, we can assign values to variables using the assignment operator =, 

# a local variable:
# a local variable is variable that is defined within  a function and is only accessible with in
# that function. it is created when the function is called and is destroyed when the function returns.

# on the other hand, a global variable is a variable that is defined outside a function and is accessible from within any function in your code.

x=4
print(x)

def hello():
    x = 5
    print(f"this is local x {x}")
    print("hello rohit")
    
print(f"the global x is {x}")
hello() #here the hello() is the function call if you dont call the function the function will not be executed.



# another example

x = 10 # global variable

def mufunc():
    global x  #her ethe global x makes changes in thw global value of x means our global value is 10 and the value we mentioned in global x is 4 it changes to 4
    x =4
    y=5 #local variable
    print(y)
    
mufunc()
print(x)
# print(y) #here when we give th eprint y it throws an error say not accessible outside the function.
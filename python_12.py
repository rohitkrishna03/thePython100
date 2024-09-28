# functions in python 

#  a block o f code that performs a specific task whenever it is called.
# in bigger programs , whenever large amount of code , it is advisibke to create are use existing functions that makes the program 
# flow organized and neat.
# there are two types of function
#  - built in function
#  - user define function

# a =9
# b =8
# gmeans1 =(a*b)/(a+b)
# print(gmeans1)
# if teh above code is considered as dlogin to find mean change the above into logic by using it def

# so you can use it for an  thing
# we will create a function by using the df key word



def caluculatemean(a,b):
    mean = (a*b)/(a+b)
    print(mean)
    
def isGreater(a,b):
        if(a>b):
            print("first number is greater")
        else:
            print("second number is greater")
    
a=9
b=8
caluculatemean(a,b)
isGreater(a,b)
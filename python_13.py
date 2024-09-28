# here we use the function argument and return statement
# there are four type of argument that we can provide in functions
# default argument
# keyword argument
# variable argument
# required argument


# default argyment

# def name(fname, mname , lname ):
#     print("hello", fname, mname, lname)
# name("rohit", "krishna", "rohi")

# taking average of numbers
import numbers
def average(*numbers):
  sum = 0
  for i in numbers:
    sum = sum + i
  print("average is :", sum / len(numbers))
average(10, 5)
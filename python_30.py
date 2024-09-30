# raising custom errors in python

# In python, we can raise custom errors by using the "raise" keyword
# in the previous method, we learned about different built in exceptions in python and why it is important to handle exceptions.add(element)
# however, sometimes we may need to create our own custom exceptions that serve our purpose.

a = int(input("enter any value between 5 and 9 :"))

if(a<5 or a>9):
    raise ValueError("value should be between 5 and 9")
else:
    print("valid value")
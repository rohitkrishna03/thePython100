# exceptional handling 
# exceptional handlinh is the process of responding to unwanted or unexpected events when a computer program runs.add(element)
# exceptional handling deals with these events to avoid the program od system crashing, and without
# this process exception would disrupt the normal operation of a program
# exception handling in python
#  ==python has many built in exceptions that are raised when your program encounters an error/ something in ptogram goes wrong
#  ==when the exception occurs, the python interpreter stops the current process and pass it to the calling process unitl it handled. if not handled the program will crash
#  == python try..except => try except are used in python to handle error and exception, the code in try block runs
# when there is no error. if the try block catches the error, then the except block is matched.add(element)
a = input("enter any number :")
print(f" multiplication table of {a} is :")
try:
    for i in range(1, 11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except:
     print("invalid input")
     print("some imp line of code")
# # finally clause:
# # the finally code block is also a part of exception handling, when we handle exception using the try and except block, we can include a finclly block at the end
# # The finally block is always executed, so it is generally used for doin the concluding t\tasks like closing file resources or closing databaase connection or may be ending the program execution with delightful message.


# try:
#  l = [1,3,5,7] 
#  i = int(input("enter any index number :"))
#  print(l[i])
# except:
#     print("index no exceeded")
# finally:
#         print("i am always executed")
        
        
        
#The below is the another example using def
 
def func1():
     try:
        l =[1,3,5,7]
        i =int(input("enter any number : "))
        print(l[i])
        return 1
     except:
        print("some error occured")
        return 0
     finally:
       print("i am finally")
       
x = func1()
print(x)
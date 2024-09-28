# recurssion in python is  the process of defining somthing interms if itself.
# 
def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return n* factorial(n-1)
print(factorial(5))


# fibonaccie in python 

# f(0) =0
# f(1)= 1
# f(2) = f(1) +f(0)
# f(n)= f(n-1) + f(n-2)

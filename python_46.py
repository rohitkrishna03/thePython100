# calculator program in python 

def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

print("select operation")
print("1.ADDITION")
print("2.SUBTRACTION")
print("3.MULTIPLICATION")
print("DIVISION")

while True:
    choise =input("select options between 1/2/3/4 :")
    
    if choise in('1', '2', '3','4'):
        try :
            num1 = float(input("enter number for num1 : "))
            num2 = float(input("enter number for num2 : "))
        except ValueError:
            print("invalid input")
            continue
        if choise == '1':
            #  ("you selected multiplication")
            print(num1, '+', num2, '=', add(num1 ,num2))
        elif choise == '2':
            print(num1, '-', num2, '=', sub(num1 ,num2))
        elif choise == '3':
            print(num1, '*', num2, '=', multiply(num1 ,num2))
        elif choise == '4':
            print(num1, '/', num2, '=', divide(num1 ,num2))
    continue_cal =input("want to continue next calculation (yes/ no)? : ")
    if continue_cal == "no":
        print("game has ended")
        break
    else:
               print("invalid input")
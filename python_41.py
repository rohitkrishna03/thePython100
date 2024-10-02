# # fibonacci .series
n =int(input("enter any number here for fibonacci series :"))
num1= 0 
num2=1
next_num = num2
count =0

while count <= n:
    print(next_num, end ="")
    count += 1
    num1,num2 =num2, next_num
    next_num =num1+num2
    print()
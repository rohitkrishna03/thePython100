# break and continue
#  the break statement enables a program to skip over a part of the code.
# a break statement treminates the very loop it lies within.
for i in range(12):
    if(i==10):
     break
    print("5 x", i+1, "=", 5*(i+1))

print("end of the loop")


# here we use the break statemen t afte the 5*10 
#  like it should show like after 50  the loop is broke
for i in range (12):
    if (i ==10):
        print("skip the iteration")
        continue
    print("5 x", i, "=", 5*1) 


# python dont have do-while loop but 
# that do-while is writtent in different kind
while True:
    number =int(input("enter a positive number:" ))
    print(number)
    if not number > 0:
        break
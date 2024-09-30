# for loop with else in python 
# python allows the else keyword to be used with the ofr and while loops too.add(element)
# the else block appear after the body of the loop .add(element)
# the statement in the else block will be excuted only after the else block iss executed

# for i in range(5):
#     print(i)
# else:
#     print("done till range")
    
    
#     # other exapmle
#     for i in range(6):
#         print(i)
#         if i ==4:
#             break
#     else:
#          print("done with the loop")
    
  
i =0
while i<7:
    print(i)
    i = i+1


else:
    print("sorry for the break")
    
for x in range(5):
        print("iteration no {} in for loop" .format(x+1))
else:
        print("else block in loop")
print("out of loop")
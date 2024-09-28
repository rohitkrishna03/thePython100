# # match case statement in python
# import os
# print("hello world")
# os.system("python --version")
# # a match statement ill compare a goven variables values of differenct shapes, also refered to as the pattens.add(element)
# # teh main idea is to keeo on the comparing the variabes with all the present patterns until it fits into one.
# #  match case consist of three main enteties
# #  -the match keyboard
# #  - one or more case clauses
# #  - expression for each case

x = int(input('enter any the value of  x: '))
match x:
  case 0:
     print('x is zero')
  case 4:
      print('case is 4')
  
  case _ if x!=90:
      print(x, 'is not 90')
  case _ if x!=80:
      print(x, 'is not 80')   
  case _:
      print(x)

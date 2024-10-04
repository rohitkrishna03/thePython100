# python pattern programming 
# all kinds of pattern programming
# simple pyramid
for i in range(10):
     for j in range(i+1):
         print("#", end=' ')
     print()
     
# #     #  simple inverted pyramid
    
for i in range(10,0,-1):
    for j in range(i,0,-1):
        print('@', end=" ")
    print()  
    
#     # pyramid of numbers
for i in range(1,10):
    for j in range(i):
        print(i, end=" ")
    print()
    
    # number inverted pyramid
    
for i in range(10,0,-1):
        for j in range(i):
            print(i, end=" ")
        print()
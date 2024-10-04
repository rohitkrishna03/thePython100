for i in range(1,6):
    for j in range(5,i,-1):
        print(".", end= " ")
    for k in range(1,i+1):
        print("*", end =" ")
    print()
print("here the dot(.) represents the empty space")    

# the below is the reverse inverted pyramid pattern
for i in range(5,0,-1):
    for j in range(5,i,-1):
        print(".", end= " ")
    for k in range(1,i+1):
        print("*", end =" ")
    print()
# # another pattern types

for i in range(1,6):
    for j in range(1, i+1):
        print(j , end=" ")
    print()
    
    
# # reversing the number pyramid 
for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j, end=" ")
    print()
    
# # 
for i in range(1,6):
    for j in range(i,0,-1):
        print(j, end =" ")
    print()
    
# =======================
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j, end =" ")
    print()
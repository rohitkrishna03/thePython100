

# Downward half-Pyramid Pattern of Star
# Pattern: –

# * * * * *  
# * * * *  
# * * *  
# * *  
# *
# n = int(input("enter any number :"))
# for i in range(n+1,0,-1):
#     for j in range(0,i-1):
#         print("@" ,end=" ")
#     print(" ")
    
# for i in range(1,n):
#     for j in range(1,i+1):
#         print("!", end =" ")
#     print(" ")


num =int(input("enter any number :"))
m= (2*num)-2
for i in range(0, num):
    for j in range(0,m):
        print(end=" ")
    m = m -1
    for j in range(0, i+1):
        print("*", end= " ")
    print(" ")

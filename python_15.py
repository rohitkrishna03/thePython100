# list methods in python
l =[11,45,1,2,3,4,1,1,1]
print(l)
l.append(7)
print(l)
l.reverse()
print(l)
print(l.index(1))
print(l.count(1))
# the above one orints how many times doe the number "1"
# is repeated


# copiying elements
m =l
m[0] =0
print(l)
m=l.copy()
m[0] =0
print(l)
print(m)

# insert
m = [900,1000,1100]
l.extend(m)
# print(l)in the above code we copy the m elements into l

# set methods in python 
# sets in oython works as sets in maths
# we perform operation slike union and intersection in the sets just like in maths.
# union() and update()
# here the methids union() prints all the things present in a and b 
# and the word itersction means ut prints same thinsg avaliable in both sets


# union and nunion-update
s1 = {1,2,3,4}
s2 = {3,6,7}
print(s1.union(s2))
print(s1, s2)

# another example for union
cities1 ={"hyderabad", "tokyo", "delhi"}
cities2 ={"tokyo","deoul","kabul","madrid","hyderabad"}
cities3 = cities1.union(cities2)
print(cities3, "this is union")

# another example for intersection
cities1 ={"hyderabad", "tokyo", "delhi"}
cities2 ={"tokyo","seoul","kabul","madrid","hyderabad"}
cities1.intersection(cities2)
print(cities1, "this is intersection")

# another example for intersection_update
cities1 ={"hyderabad", "tokyo", "delhi"}
cities2 ={"tokyo","seoul","kabul","madrid","hyderabad"}
cities1.intersection_update(cities2)
print(cities1, "this is intersection update")

# another example for symmetric_intersection
# the things symmetric diff means which are not common in the both a sections
cities1 ={"hyderabad", "tokyo", "delhi"}
cities2 ={"tokyo","seoul","kabul","madrid","hyderabad"}
cities3 = cities1.symmetric_difference(cities2)
print(cities3, 'this is symmetric difference')
cities1.add("berlin")
print(cities1)
# cities1.clear()
# print(cities1)
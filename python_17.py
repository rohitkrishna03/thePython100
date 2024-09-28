# manipulating tuples

# tuples are immutable. hence if you want to add, remove or change tupleitems, then first you must convert the tuple to list. then 
# perform operation on that and convert it back to tuple.

# countries =("spain", "italy", "india", "england", "germany")
# temp =list(countries)
# temp.append("russia") #adds russia
# temp.pop(3) #removes 3 item in index
# temp[2] ="finland" #replaces item 
# countries=tuple(temp)
# print(countries)

tuple1 = (0,1,2,3,4,3,5,6,3,7,8)
res=tuple1.count(3)
res=tuple1.index(3)
res = tuple1.index(3,4,8)
res =len(tuple1)
# here in the above code we can see 3,4,8 which means 
# it searches for 3 which comes after 4 th indes in which position before 8 th index.
print('count of 3 in tuple :', res)




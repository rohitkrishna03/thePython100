# #  her ewe will learn about mao , l=filter, and reduce functions in python 
# # in python, the map filter nad reduce functions are built in functions that 
# # allows you to apply the function to a sequence od elements and return a new sequence.
# # those functions are called as high order functions, as they a=take other function as segment.


# #map()
# # the map function applies  applies the function to each elemsnt in a sequence and return a new sequence containin g the transformed element
# #map function has following syntax

# # map(function, iterable)

def cube(x):    
    return x * x * x

# print(cube(8))

# l =[1,2,3,4,5,6]
# # newl =[]
# # for item in l:
# #     newl.append(cube(item))
# # print(newl)
# newl = list(map(cube, l))
# print(newl)
    
    
    
# filter()
# filter is the function od sequence of elemsnts on agiven predicate and retuen a new function containing only the elemsnts that meeet the preducates 
# the filter function has the following syntax
# filter (predicate, iterable)

l =[1,2,3,4,5,6]
newl = list(map(cube, l))
print(newl)

def filter_function(a):
    return a>2
# means it only takes the values that are greater than a in th elist 
newnewl = list(filter(filter_function, l))
print(newnewl)

# reduce()
# here the reduce function whill summ the whole list and make it into single number.

from functools import reduce
numbers =[1,2,3,4,5,6]

def mysum(x,y):
    return x+y
sum = reduce(mysum, numbers)
print(sum)

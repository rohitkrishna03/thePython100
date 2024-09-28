# string slicing and operation on strings
# in this we can find the length of the string by isng the len() method
# name ="rohit, krishna"
# print(name[0:5])
# # here the thing [0:5] only prints from 0 index to 5 index which is rohit
# # if we want the lenfth of the names
# print(len(name))
# # which prints 14 in th o/p 

# a ="hammer"
# len1 = len(a)
# print('the word hammer has', len1, 'letters')

# ve use square bracates for slicing the word like
c = "flowers"
flen = len(c)
print(c)
print(c[0:3])
# here now we see about the negative indexing
print(c[:-3])
# in the above indexing which is [:-3]
# what it actuallt does is even if we dont give o before -3 
# it automatically takes len(c)-3 into consideration
print(c[0:len(c)-3])
print(c[-3:-1])
# which prints from last liel -3 means e nad -1 means r ans the output will be er
nm='rohit'
print(nm[-4:-2])
# here in the baove code there is rohit with slicing -4:-2
# where -2 means it will exclude -2 from ending of rohit rohit-2 = roh
# and hwhere -4 it will which is to print the word which is in the index of -4 which is in -4 index there is which is o
# nad -4:-2 means -4 is the starting od the string nad -2 is index of the string that is reamined after excluded
# so - 4 means o nad -2 means h
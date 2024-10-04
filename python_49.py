# slicing in python 

# In python slice can be done in 2 ways :
# using a slice() method 
# using the array slicing [::] method

# for the first method
# slice(stop)
# slice(start, stop , step)
string  = "rohit"
s1 = slice(3)
s2 = slice(1,5,2)
s3 = slice(-1,-12,-2)
s4 =slice(0,-1,2)
print("string slicing")
print(string[s1])
print(string[s2])
print(string[s3])
print(string[s4])
print(string[1:-1])
# arr[start:stop]         # items start through stop-1
# arr[start:]             # items start through the rest of the array
# arr[:stop]              # items from the beginning through stop-1
# arr[:]                  # a copy of the whole array
# arr[start:stop:step]    # start through not past stop, by step


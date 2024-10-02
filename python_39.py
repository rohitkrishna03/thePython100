# a file manipulating technique

# before we can perform any operation on a file , we must first open it, python provides the open() function
# to open a file.add(it takes two arguments )
# the name of the file and the mode in which the filr should be opened
# the mode can we reading , writing , appending.

f =open('python_38.py', 'r')
# print(f)
text = f.read()
print(text)
f.close()
# the above code is to read the test which is there in th file.

# if we want to open any image file like jpg png or pfd we nee to use rb in th aplace of r


# if we want to add any data into that file we need to write int that file

# # f =open('python_38.py', 'r')
# f.write('hello world)
# f.close()
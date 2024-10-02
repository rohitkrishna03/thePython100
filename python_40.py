# readlines() method 
# the readlines() method reads a single line from the file . if  we want to read multiple lines, we can use a logo.
# writelines() method
# the writelines() method
# the writelines(method in python writes a sequence of strings to file. the sequence can be any iterable object,
# such as a list or a tuple.
# here we will create a file stud.txt
f= open('stud.txt', 'r')
i = 0
while True:
    i = i+1
    line = f.readline()
    if not line:
        break
   
    m1 = line.split(",")[0]
    m2 = line.split(",")[1]
    m3 = line.split(",")[2]
    print(f"marks of the student {i} is {m1}")
    print(f"marks of the student {i} is {m2}")
    print(f"marks of the student {i} is {m3}")
  
    print(line)
    
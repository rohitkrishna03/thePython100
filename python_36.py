# os module in python 

# the os module in python in a built-in library that provides function for interacting with the operating system.
# it allows you to perform a wide variety of tasks, such as reading and writing files.

# reading and writing files , the os module provides functions for opening, reading and writing files.
# for example, to open a file for reading, you can use the open function.

import os 
# os.mkdir("data")

#which creates folder named data in the present folder.

# if(not os.path.exists("data")) :
#        os.mkdir("data")
# for i in range(0,100):
#         os.mkdir(f"data/Day{i+1}")
# and we can see in the above code that we can create 100 folders with the name day
# below we will see how to change the name of the folder 
# the folder name is day and we will change them into 
# for i in range(0,100):
#     os.rename(f"data/day{i+1}", f"data/class{i+1}")
    
folders = os.listdir("data")    
print(folders)
print(os.getcwd())

# # the above on prints is there is any data/files/folders in the folder
# for folder in folders:
#     print(os.listdir(f"data/{folder}"))
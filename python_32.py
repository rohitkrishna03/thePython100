# ENUMERATE FUNCTION IN PYTHON

# the enumerate function in a built-in function inpython that allows you to over a sequence(such as list, tuple or string) and get the index and value of each element in the sequence at the same time.

# marks =[12,56, 32, 98, 12, 45, 1, 4]
# index =0
# for mark in marks:
#     print(mark)
#     if(index ==3):
#         print("ended here")
#     index +=1
    
    # in the below example we use enumerated function
marks =[12,56, 32, 98, 12, 45, 1, 4]
for index, mark in enumerate(marks, start =1):
        print(marks)
        if(index ==3):
            print("harry, awesome!")
    
    
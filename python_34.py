#HOW IMPORTING IN PYTHON WORKS

# importing in python is the process of oading code from a python module into the current script.
# this allows you to use tye function and variable defined in the module in your current script, as well as any additional modules that the imported may depend on.
# 
# to import a module in python, you use the import statement followed by the name of the module.add(for example, to import the math module, which contains a variety of mathamateical function, you would use the following statement.


#below is the example for import

import math as m 
result = m.sqrt(9) * m.pi
print(result)


#to see what are the functions psresent in math function

print(dir(m))

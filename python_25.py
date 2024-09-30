# python dictionaries
# dictionaries are ordered collection of data items.
# they are stored multiple items in a single variable
# dictionary items are key-value pair that are separated by commas and enclosed within curly brackets

info ={'name':'rohit', "age":25, "eligible": True}
print(info)
print(info['name'])
print(info.keys())


print(info.items())
for key, values in info.items():
    print(f"the values corresponding to the key{key} is {values}")
    
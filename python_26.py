# python dictionary methods
# dictionary uses several built-in methods for manipulation. they are listed below
ep1 = {122:45, 123:23,567:89}
ep2 = {222:67, 2354:90}
ep1.update(ep2)
ep1.clear()
ep1.pop(122)
ep1.popitem()
del ep1[122]
print(ep1)
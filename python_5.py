# string methods in python 
# finding the length of the string 
# changing the string into upper case and lower case
# strings are immutable
a = 'rohit'
# rlrn = len(a)
print(a.upper()) #this changes the string into upper case 
print(a.lower())

b = 'lion!!!!!!'
print(b.rstrip("!"))
# here the rstrip removes the mentioned character or letter or any 
print(a.replace("rohit", "krishna"))
# here th replace method replaces rohit with krishna

c= "there are many cars"
print(c.split())
# which splits into list

# bold heading
boldHeading = "introduction To Python"
print(boldHeading.capitalize())
# here its captalises the starting letter of the statement 

# count
d ='car is a car which is a car and a car'
print(d.count('car'))
# which tell how may times os the car repeated

# if you want to end a sentence or a statement with anything to check weather the sentece ends whith the given string 
# here i gave !! which doesnot exist in the str1 so it prints false in the output
str1 ="welcome home guys"
print(str1.endswith('!!!'))


str = "welcome to the cinema"
print(str.endswith("to", 4, 10))

# to find index in the string

str3 = "welcometothescaryhouse"
print(str3.find("the"))
# the abive in eprints the indes of the
# to check the above string contains only alphabets
print(str3.isalpha())

str4 ="Wealth Of Orginization"
print(str4.istitle())
# the above one checks the title has upper case alpha in the staring i fthe owrd.

# check if the sentence starts with particular string 
print(str4.startswith('Wealth'))

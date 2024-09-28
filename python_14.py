# python list 
# lists are ordered collection of data items
# they store multiple items in a single variable
# list items are separated by commas and enclosed within square brackets []
# list are changeable meaning we can alter them after creation
marks = [3,4,5, "tom"]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])

# negative indexing :
# similarly to positive indexing, negative indexing is also used to access items, but from the end of the list. the last item has index[-1], second last item has index[-2],,
# third last item has index[-3] and so on.add(element)
marks = [3,4,5,"tom","jerry"]
print(marks[-3])
print(marks[len(marks)-3])
print(marks[5-3])
print(marks[2])
if 'tom' in marks:
    print('true')

# list comprehension
# list comphrehension are used for creating new list from other iterable like lists,
# tuples, dictionaries, sets, and even in array and string.
lst =[i*i for i in range(10)]
print(lst)
lst = [i*i for i in range(10) if i%2==0]
print(lst)
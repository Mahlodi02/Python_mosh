# DICTIONARIES {}
'''Is collection of key-value pairs which is ordered* and changeable.
we often use strings and numbers for keys but we can any type'''

# we have function called dict(), same as list() and tuple()
# Different ways to create a dictionary
person = {'name': 'John', 'age': 30}  # using curly brackets
print(person)
person2 = dict(name='Jane', age=25)    # using dict() constructor
print(person2)
person3 = dict([('name', 'Doe'), ('age', 40)])  # using list of tuples
print(person3)

# ACCESSING ITEMS
print(person["name"]) # to get value of index 1 but here index is the key 
for key in person:
    print(key)

person['name'] = 'Mike'  # updating value
print(person)
person['city'] = 'New York'  # adding new key-value pair
print(person)
del person['age']  # deleting key-value pair
print(person)

# for key, value in person.items(): # looping through key-value pairs
#     print(key, value)


if "province" in person: # checking if key exists
    print("Yes")
else:
    print("No")

# DICTIONARY COMPREHENSIONS
values = []
for x in range(5):
    values.append(x * 2)
print(values)

# remeber list comprehension is like this
# [expression for item in items]
values = [x * 2 for x in range(5)]
print(values) # and if we wrap it into curly brackts we get sets

# to make it a dictionary comprehension we need to have key-value pairs
values_dict = {x:x *2 for x in range(5)}
print(values_dict)

# we use comprehensions when we see loop of iterable, list,set,dictionary
    
# UNPACKING OPERATORS **
'''An operator that handy when working with data structure in python.'''
numbers = [1, 2, 3] # lets say we want items in list individually
# we can unpack them like this
print(*numbers)  # will print 1 2 3, prefixing the list with * astrisk

# lets create a list
more_numbers = list(range(5))
print(more_numbers)

# instead of this, we have the other way using unpacking operator
nums = [*range(5), *"Hello"] # will unpack the range and the string into individual items
print(nums)

# we can even combine multiple list uding unpacking operator
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = [*list1,"a", *list2, *"mahlodi"] # we can unpack multiple list and evrn add other items
print(combined)

# now lets unpack a dictionary, but to do that we use ** double astrisk
first = {'name': 'John'}
second = {'age': 30}
combined_dict = {**first, **second, 'city': 'New York'} # we can also add other key-value pairs
print(combined_dict)
# we use unpacking operator to take out the individual values in any iterable
# we can also use it to combine multiple data structures
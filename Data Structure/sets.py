# SETS {}
'''Is a collection which is unordered, unchangeable*, and unindexed and no duplicates. 
In Python sets are written with curly brackets.'''

numbers = {1, 1, 2, 3, 4, 5}
unique_numbers = set(numbers) # will return a set of new numbers wrapped in curly brackets
print(unique_numbers)
# You can still append, remove, delete, however yu cant use indexing

seconnd = {2,6}
print(unique_numbers | seconnd) # union of two sets
print(unique_numbers & seconnd) # intersection of two sets
print(unique_numbers - seconnd) # difference of two sets
print(unique_numbers ^ seconnd) # symmetric difference of two sets

# Sets are best for mathematical operations involving multiple sets such as union, 
# intersection, difference, and symmetric difference.
# They are also useful for removing duplicates from a collection since sets automatically
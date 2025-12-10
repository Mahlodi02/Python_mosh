'''Different ways to create a list in python
1. Using square brackets [] and inside the square brackets we can have a list of any type
strings, numbers, booleans and a mix of all these types
2. Using the list() constructor'''

letters = ['a', 'b', 'c'] 
matrix = [[0,1], [2,3], [4,5]] # list of list, two dimensional list
zeros = [0] * 5  # creates a list with 5 zeros
combined = letters + zeros  # concatenating two lists
numbers = list(range(20))  # creates a list of numbers from 0 to 19
chars = list('Hello World')  # creates a list of characters from the string

len(letters)  # returns the length of the list


# ACCESSING ITEMS
'''We can access items in a list using their index.'''
print(letters[0])  # first item
print(letters[-1])  # last item

# SLICING
'''We can access a range of items in a list using slicing.'''
print(letters[0:2])  # items from index 0 to 1
print(letters[:3])  # items from start to index 2
print(letters[1:3:2])  # items from index 1 to 2 with a step of 2

# LIST UNPACKING
'''We can unpack a list into individual variables.'''

nums = [1, 2, 3]
a = nums[0]
print(a)
b = nums[1]
print(b)
c = nums[2]
print(c)

# there is better and cleaner way to do this
x, y, z, = nums  # unpacking
print(x, y, z)


# LOOPING OVER A LIST
'''We can loop over a list using a for loop.'''

characters = ['a', 'b', 'c', 'd']
for char in characters:
    print(char)

#  we can also use the enumerate function to get the index and the item
for index, char in enumerate(characters):
    print(index, char)

# ADDING AND REMOVING ITEMS
# TUPLE ()
'''Tuples is a collection which is ordered and unchangeable. 
In Python tuples are written with parenthesis.'''

# Different ways to create a tuple
point = (1, 2)               # Using parentheses
print(point)          
point2 = 1, 2                # Without parentheses
print(point2)         
point3 = 1,                  # Single element tuple (note the comma)
print(point3)
point4 = tuple([1, 2, 3])  # Using the tuple() constructor list to tuple
print(point4)
point5 = tuple(("Hello world")) # Using the tuple() constructor string to tuple
print(point5)

# we can use indexing and slicing just like lists to access elements in a tuple
print(point[0])          # Accessing first element
print(point[0:2])       # Slicing the tuple

# we can unpack tuples into variables
x, y = point
print(x, y)

# we can also use in operator to check if an element exists in a tuple
if 6 in point:
    print("True")
else:
    print("False")


# SWAPPING VARIEBLES

a = 1
b = 2
 # lets can have another varieble c to swap a and b
# c = a
# a = b
# b = c
# print(a, b)

# but in python we can do it in a single line without using another varieble
a, b = b, a
print(a, b)

# ARRAYS
'''we use arrays when working with large data sets of numerical values.
Arrays are more efficient than lists in terms of memory and performance.
to use arrays in python we need to import array module
Arrays can only store elements of the same data type.'''

from array import array
# creating an array of integers
nums = array('i', [1, 2, 3, 4, 5])
print(nums)

nums.append(6)          # Adding an element to the end of the array
print(nums)
nums.pop()              # Removing the last element from the array
print(nums)
nums.remove(3)          # Removing an element from the array
print(nums)
if 10 in nums:      # Checking if an element exists in the array
    print("True")
else:
    print("False")




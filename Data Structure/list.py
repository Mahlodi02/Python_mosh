# LISTS []
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
letters = ['a', 'b', 'c']
print(letters)
letters.append('d') # add the d at the end of the list
print(letters)
letters.insert(0, 1) # add one at the index 0
print(letters)

# remove items
letters.pop() # removes the lats item in a list
print(letters)
letters.pop(0) # removes item at index 0
print(letters)
letters.remove('b') # use remove item in a list when you don't know the index
print(letters)

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
del alphabets[0] # you can also use delete statement to remove an item at from a list, 
                    #deletes item at index 0
print(alphabets)
del alphabets[2:4] # deletes items from index 2 to 3
print(alphabets)

alphabets.clear() # removes everything in a list
print(alphabets)

# FINDING ITEMS
'''Let's say you want to find item at a particular index
or checks if the item exists in a list'''

numbers = [1, 2, 3, 4, 5]
print(numbers.index(2))  # returns the index of the item 2
# print(numbers.index(6))  # throws an error since 6 is not in the list
# you can use the in operator to check if an item exists in a list instead of using indexing to avoid error message
if 6 in numbers: # checks if 6 exists in the list
    print("True")
else:
    print("False")


# SORTING A LIST
'''We can sort a list using the sort() method or the sorted() function.'''

values = [5, 3, 8, 1, 4]
values.sort() # sorts the list in to ascending order
print(values)
values.sort(reverse=True) # sorts the list in to descending order
print(values)

# we also have sorted() method which returns a new sorted list
values = [5, 3, 8, 1, 4]
new_values =sorted(values) # returns a new sorted list in ascending order
print(new_values)
reversed_new_values = sorted(new_values, reverse=True) # returns a new sorted list in descending order
print(reversed_new_values)

# if we have a list of complex items like list of turples

items = [('product1', 10), ('product2', 9), ('product3', 12)]
items.sort() # it will return as it is
print(items)

# so for us to be able to sort the items we need to create a function that will help us sort items in the list
def sort_item(item):
    return item[1]  # sorts by checking the number/price of the product

items.sort(key=sort_item) # sorts the list using the sort_item function
print(items)

# but is better and cleaner way to do this by using lambda function
# lambda function is simple one line anonymous function that we can pass to another function

#items.sort(key=lambda parameter: espresion) # syntax of lambda function

items.sort(key=lambda item: item[1]) # sorts the list using the lambda function
print(items)

# MAP FUNCTION
'''let's say we want to transorm  list of itms in defferent shape and remember each item in a list 
is a tuple with product name and price
> let's say our main inerest is the items price and lets trsnsform them into a list'''

prices = []
for item in items:
    prices.append(item[1])  # appending the price of each item to the prices list
print(prices)

# there is better way to do it by using map function
prices = list(map(lambda item: item[1], items)) # usinf map function to get list of price and wrap it to list funtion to convert it into list
print(prices)

# FILTER FUNCTION
'''Noe lets filter the list of items and get the products that are greater than or equal to 10'''
filtered_items = list(filter(lambda item:item[1] >=10, items)) # using filter functions and wrapping it into list function to make it a list
print(filtered_items)

# LIST COMPREHENSION
'''we have another way instead of using map and filter functions we call that list comprehension'''

#[expression for item in items] > this is the stracture for list comprehension

prices = [item[1] for item in items] # list comprehension to get list of prices
print(prices)

filtered_items = [item for item in items if item[1] >= 10] # list comprehension to get list of items with price greater than or equal to 10
print(filtered_items)

# ZIP FUNCTION
'''Now we have two lists and we want too combine them into one list of tuples , by index position in each tuples'''

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

combined = list(zip(list1, list2)) # using zip function to combine two lists
print(combined)

# STACKS
'''A stack is a data structure that follows the Last In First Out (LIFO) principle.'''
browsing_session = []
browsing_session.append(1) # user visits page 1
browsing_session.append(2) # user visits page 2
browsing_session.append(3) # user visits page 3
print(browsing_session)
browsing_session.pop() # user clicks the back button
print(browsing_session)
if not browsing_session:
    browsing_session[-1] # checking if the stack is empty before popping an item


# QUEUES
'''A queue is a data structure that follows the First In First Out (FIFO) principle,
for you to be able to perform queue you need to import its module from collectons.'''

from collections import deque
queue = deque([])
queue.append(1) # user 1 joins the queue
queue.append(2) # user 2 joins the queue
queue.append(3) # user 3 joins the queue
print(queue)
queue.popleft() # user 1 is served and leaves the queue
print(queue)
if not queue:
    print("Queue is empty") # checking if the queue is empty before popping an item
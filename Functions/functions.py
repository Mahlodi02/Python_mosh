"""FUNCTIONS"""

# DEFINING FUNCTION

def greet():
    print("Hi")
    print("Welcome aboard")

greet() # don't forget to call your function


# ARGUMENTS

# Difference bettween print and greet function is that..
# print function take input , while greet function take parameters and when we call the funtion the parameters are required , and we call those parameters that we are passing argumnets

def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard!!..")

greet("Mahlodi", "Seitsiro")


# TYPE OF FUNCTIONS
'''1. Function that perform a task
    2. Function that return  a value'''

def greet(name):
    print(f"Hi {name}")  # in this function you are locked in printing something in the terminal, in future when you ehat to sent messege to filr or email you can't mraning you have to create another function

greet("Mahlodi")


def greeting(name):
    return f"Hi {name}"  # here we can print it in terminal , open it inside file


message = greeting("Mahlodi")
print(message)   

file = open("content.txt", "w")
file.write(message)


# DEFAULT ARGUMENTS
'''Now lets make parameter optional
All parameters you define in a fuction are required by default
if you don't want to explicitly pass by=1 everytime we call this increment function
you need to give the parameter a default value'''

def increment(number, by=1): # Remember the optional parameter should always come after the required parameters
    return number + by

print(increment(2,5))


# XARGS
'''There's time when you what to create a function that take variable number arguments'''

def multiply(x, y):
    return x * y

print(multiply(2,3))

# But now let's say you want to pass multiple numberss

def multi(* numbers):
    total = 1
    for number in numbers:
        total *= number
    return total
print(multi(2,3,4,5))
# here the * before numbers allow us to pass multiple arguments and inside the function we can iterate over them like a list

# XXARGS
# We can use ** args to pass multiple key-value pairs
def save_user(** user):
    print(user)
save_user(id=1, name="Mahlodi", age=24)
# it will return a dictionary with key-value pairs

# SCOPE
'''Scope refers to a region of code where the variable is defined.
There are two main types of scope in Python: global scope and local scope.'''

# LOCAL SCOPE
'''is a variable defined inside a fuction and can only be accessed inside that function'''
def greet():
    mssg = "Hello"
    print(mssg)

# greet()
# print(mssg) # this will raise an error because message is not defined outside the function

# GLOBAL SCOPE
'''is a variable defined outside any function and can be accessed anywhere in the code'''

greeting = "Hello everyone"

def greeting_people():
    print(greeting) # accessing global variable inside function

greeting_people()
print(greeting) # accessing global variable outside function


# DEBUGGING
# Debugging is the process of finding anfd fixing errors(bugs) in your code
# When your program crashes , give wrong results, you need to debug to find whats wrong and how to fix it


# def divide(a, b):
#     return a / b
# print(divide(4, 0))  # this will raise an error because we can't divide by zero
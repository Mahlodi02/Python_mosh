students_count = 1000 # intiger
rating = 4.99         # float number
is_published = True   # boolean
course_name = "Python Programming" # string

'''we seperate two words with underscore because in python
    we can't have space betwween two words'''

# STRINGS
course_name = "Python Programming" # string
print("#" * 20)
# When working with text you should surround it with qoutes
# You can use  single or double qoutes 
# We also have triple qoutes that we use to format a long string or mutiple lines

# message = '''
# Hi Tt

# I hope you are well.

# Thank you'''

## THINGS WE CAN DO WITH STRINGS ##
'''we have the buil-it function for getin g the length of strings in python

Funtion > A function is reusable piece of code that can carries  out  a task '''

print(len(course_name)) # len stands for length , is a build-in fuction in python to get the length of a string
print("#" * 20)
# to get the specific charecter 

print(course_name[0]) # first charecter of a string
print(course_name[-1]) # Last charecter of a string
print(course_name[0:3]) # slicing a sting 
print(course_name[0:]) # starting from indexs 0 to end
print(course_name[:3]) # starting from index 0 to index 3
print(course_name[:]) # it will outcome the copy of course_name
print("#" * 20)   

# ESCAPING SEQUENCES
course_name = "Python \"Programming" # when you eant to have double qoutes inside double qoutes
print(course_name)
course_name = "Python \'Programming"  # when you want to have single qoutes inside single qoutes
print(course_name)
course_name = "Python \\Programming"  # when you want to have backslash
print(course_name)
course_name = "Python \nProgramming"  # when you want to have newline
print(course_name)
print("#" * 20)

# FORMATTED STRINGD

first = "Mahlodi"
last = "Seitsiro"
# full = first + " " + last # we can concatinate by using addition sign
full = f"{first} {last}" # here we are using formatted strings can be lowercase f"" of upercase F""   and use curly braces {}
print(full)
print("#" * 20)
# STRING METHODS
# Here will be looking into few useful functions available to work with strings
course_name = "Python Programming" # string
# if you type course_name. you'll see all available functions on strings
# in formal way we refer to this function as methods, is a term in object oriented programming(OOP)
# Everything in python is an object and object have a functions we call methods that we can access using the dot notation

print(course_name.upper()) # covert string text to uppercase
print(course_name.lower()) # convert text to lowercase
print(course_name.title()) # convert every first letter of word in to capital letter
print(course_name.strip()) # remove spaces start and end
print(course_name.rstrip()) # remove spaces on the right
print(course_name.rstrip()) # rmove spaces on the left
print(course_name.find("Pro")) # checks for Pro
print(course_name.find("pro")) # checks for pro
print(course_name.replace("p", "j")) # replace every p in string with j
print("pro" in course_name) # will check if pro is there on the string and print true or false
print("swift" not in course_name) # will check whether swift is not in the string and print true or false


print("#" * 20)
# NUMBERS

'''In python we have 3 types of numbers'''

# x = 1 # integers
# x = 1.1 # float
# x = # a + bi where i is imaginary numver (complex number)

# #syntax for representing complex number

# x = 1 + 2j

# this are all 3 tyoes of numbers we have in python , and we have standard arithmetic operations that we have in maths
# addition +
#subtraction - 
# multiplication *
# two types of division
  # / will give you float number
  # // will five you an integer number
# modulus % which is the remainder of devision
# exponents **

print(10+3) # addition +
print(10-3) #subtraction - 
print(10*3) # multiplication *

 # two types of division
print(10/3) # / will give you float number
print(10//3) # // will five you an integer number

print(10%3)  # modulus % which is the remainder of devision
print(10**3) # exponents **

print("#"*20)

# WORKING WITH NUMBERS

# Python has a maths module that include lots of mathemetical functions
# you need to import it to have assess to this maths funtions

print(round(2.9))
print(abs(-2.9))
import math

# when you type math. you will see all functions that maths modules

print("#" * 20)


# Type CONVERSION

# we use input function to get input from the user
x = input("x: ") # you dont run this program using code runner
print(type(x)) # to check type x, whether is
# str(X) x to string 
# int(X) x to integer
# bool(X) x to bool
# float(X) x tto float
y = int(x)+ 1
print(f"x: {x}, y: {y}")
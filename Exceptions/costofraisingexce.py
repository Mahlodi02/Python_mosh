"""Lets start by importin the module that will help us to calculate execution of some pythone code
with the previous code on raisingexceptions.py"""
from timeit import timeit # with this module we can calculate the exceution time of some python code

 # now we have define a variable and set it to a string and that string should include some python code

code1 = """def calc_xfactor(age):
    if age <= 0:
        raise ValueError("Age can't be zero or less than 0")
    return 10 / age
 
try:
    calc_xfactor(-1)
except ValueError as error:
    pass
"""  # we use triple qoutes because our code spread around multiple lines

print("code1 time =",timeit(code1, number=10000)) # this  will show time it took to execute our code 10000 times . but if we do not print the error message we raised our time will be less

""" Now instead of raising a error message lets return none"""

code2 = """def calc_xfactor(age):
    if age <= 0:
       return None 
    return 10 / age
 

xfactor = calc_xfactor(-1)
if xfactor == None:
    pass

"""
# Here we don't need try block we can simple store our value into variable and compare it to none and just pass
# this code will have less time of execution

print("code2 time=",timeit(code2, number=10000))
# Raising Exceptions
"""You can raise an exception at your on code"""

def calc_xfactor(age):
    if age <= 0:
        raise ValueError("Age can't be zero or less than 0")
    return 10 / age
 
try:
    calc_xfactor(-1)
except ValueError as error:
    print(error)

# But theres cost to doing this check on costofraisingexce.py file
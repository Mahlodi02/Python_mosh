# Handling Different Exceptions
"""Now eith the sme code we wrote on the handlingexceptions.py let's add another line
of code that might cause error when we execute the our code """

try:
    age = int(input("Age: "))
    xfactor = 10 / age # this will raise this type of error message "ZeroDivisionError: division by zero"
except (ValueError, ZeroDivisionError): # By adding this ZeroDivisionError we prevent our code to not raise this error message
    print("You didn't enter a valid age")
else:
    print("No exceptions were thrown.")

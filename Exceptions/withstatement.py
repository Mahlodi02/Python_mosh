# The with Statement
"""Instead of using finally clouse to close the external resource we have better way to do it
with the same code we used in cleanup.py file"""

try:
    # file = open("Exceptions\\cleaningup.py") 
    with open("Exception\\cleaningup.py") as file: # with this python will automatically open and close the file 
        print("file opened") # here we are just print but you can also read the content in the file and also write on the file and so on
    age = int(input("Age: "))
    xfactor = 10 / age 
except (ValueError, ZeroDivisionError): 
    print("You didn't enter a valid age")
else:
    print("No exceptions were thrown.")
# finally: 
#     file.close()  # and we do not need this as python will close it for us automatically
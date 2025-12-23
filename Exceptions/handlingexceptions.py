# Handling Exception
"""To prevent our program from the exception error we do the following"""

# age = int(input("Age: ")) # by now you knoe if the user insert or type wrong value it will raise excetiion error
"""here we will get ValueError if user input a value which is not an integer"""

try: # it shows this block of code handle errors that might occur on our code
    age = int(input("Age: "))
except ValueError as ex:
    print("You didn't enter a valid age")
    print(ex) # you can print the error
    print(type(ex)) # you can even print typy of error you have
else:
    print("No exceptions were thrown.")
    
    


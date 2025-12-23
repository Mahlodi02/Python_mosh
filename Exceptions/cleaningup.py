# Cleaning Up 
"""Sometime we are working with external resource such as file, data, network connections and so on.
 so we  need to release the when we are done so that another programs can be able to open file"""

try:
    file = open("Exceptions\\cleaningup.py") # opens the file we are working on now
    age = int(input("Age: "))
    xfactor = 10 / age 
except (ValueError, ZeroDivisionError): 
    print("You didn't enter a valid age")
else:
    print("No exceptions were thrown.")
finally: # closes the file and the end of the code , wheter the code raise and error or not it will still close the file
    file.close() 


            





# Creating a Class
"""When creating class we use pascal naming converstion.
and it's different from naming convention we use for naming variables and functions 
pascal naming convention state that the first letter of each word should be capitalized
and there shhould be no underscores between words."""

class Point:

    def draw(self): # all fuctions should have one parameter by convention which is called "self"
        print("draw")

point = Point()
point.draw()
print(type(point)) # <class '__main__.Point'> , checking the type of the object point
print(isinstance(point, Point)) # True , checking if the objcet point is an inastance of the class Point

# But our point object need some initial values like x and y coordinates. and for that we need a constructor.
# check constructor.py file 
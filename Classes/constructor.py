# Constructor -> Is a specilal method that is called when we create an object from a class.
# Self -> is a reference to the current instance of the class. It is used to access variables that belongs to the class.
"""e.g 'point = Point(1, 2)' when we call the Point class python will automatically 
call create a point object in a memory and set self to reference that point object."""
# Object can have attributes that are basically variables that include data about that object.

class Point:

    def __init__(self, x, y): # constructor method, by convention it's name is always __init__
        self.x = x # setting the attribute x of the object to the value of parameter x
        self.y = y  # setting the attribute y of the object to the value of parameter y

    def draw(self):
        print(f"Point {self.x}, {self.y}")

point = Point(1, 2) # when we create an object from the class Point we need to pass the values for x and y
point.draw() # Point 1, 2
# Magic Methods
"""Magic methods are functions/methods that start
and end with double underscores (__). And they are called
automatically by python interpreter depending on how we use
our objects and classes."""

class Point:
    
    def __init__(self, x, y): # It's called automatically when we create an object
        self.x = x
        self.y = y

    def __str__(self): # It's used to return a string representation of the object, is called when we print the object
        return f"({self.x}, {self.y})"
    
    def draw(self):
        print(f"Point ({self.x}, {self.y})")

point = Point(1, 2)
print(point)  # without __str__method this will print the module, name of class and memory address of the object
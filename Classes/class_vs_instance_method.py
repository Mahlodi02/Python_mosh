# Class VS Instance Method
"""Same as class vs instance attribute , we also have class vs instance methods
Functions/Methods that we define inside a class are Instance methods,
we call them using an instance of a class (using an object of that class)
we use this instance method whenever we need an object reference"""

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod # decorator to define a class method
    def zero(cls): # class method, we use cls as convention instead of self
        return cls(0,0) # this will return an object of the class Point with coordinates (0,0)

    def draw(self):
        print(f"Point {self.x}, {self.y}")

point = Point(1, 2) 
point.draw()  # calling instance method using an instance of the class

point2 = Point.zero() # calling class method using the class itself
point2.draw()

"""There are time we don't need an  existing object, and that's when we use a class method
e.g let's say we have a lot cases where we want to crate a point at the origin (0,0)
and we don't want to create an object every time we want to create a point at the origin
we need to define a method at class level that will retuen an object with those cooo=rdinates"""


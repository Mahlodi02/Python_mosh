# Comparing Objects 

"""At time we want to compare two objects 
e.g if we create (other = Point(1,2)) and we want to compare
it with (point = Point(1,2)) using (point == other)
By default this will return False because python compares the memory 
then we have to use magic methods called __eq__ to compare the values of the objects"""

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other): # magic method to compare two objects
        return self.x == other.x and self.y == other.y
    
    def __gt__(self, other): # magic method to compare two objects using greater than operator
        return self.x > other.x and self.y > other.y
    

point = Point(1, 2)
other = Point(1, 2)
print(point == other)  # True because we have defined __eq__ method
print(point != other)  # False because we have defined __eq__ method
another = Point(0, 0)
print(point > another)  # True because we have defined __gt__ method
print(point < another)  # False because we have not defined __lt__ method
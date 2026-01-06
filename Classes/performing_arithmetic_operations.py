# Performing Arithmetic Operations

"""We also have magic methods for performing arithmetic operations
e.g addition, subtraction, multiplication, division etc."""

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other): # magic method for addition
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other): # magic method for subtraction
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other): # magic method for multiplication
        return Point(self.x * other.x, self.y * other.y)

    def __truediv__(self, other): # magic method for division
        return Point(self.x / other.x, self.y / other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"
    
point1 = Point(10, 20)
point2 = Point(1, 2)
combined = point1 + point2  # calls __add__ method
print(combined.x, combined.y)  # 11 22
print(combined)  # (11, 22)
difference = point1 - point2  # calls __sub__ method
print(difference)  # (9, 18)
product = point1 * point2  # calls __mul__ method
print(product)  # (10, 40)
quotient = point1 / point2  # calls __truediv__ method
print(quotient)  # (10.0, 10.0)

# Note: without __str__ method this will print the module, name of class and memory address of the object
# unless you print the attributes individually like print(combined.x, combined.y)
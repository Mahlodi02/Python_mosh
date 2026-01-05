# Class VS Instance Attributes

class Point:
    default_color = "red"  # class attribute

    def __init__(self, x, y):
        # since we've difine x and y in a constructor method meaning every object we create is going to have this attributes by default
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point {self.x}, {self.y}")

Point.default_color = "blue"  # modifying class attribute, this wll change for all instances of the class

point = Point(1, 2) # 1,2 are instance of the object point
point.z = 10 # we can also define new attributes after creating an object. because in python objects are dynamic
# but this attribute z is not part of the class Point, it's only part of the object point

print(point.default_color) # accessing class attribute via instance
print(Point.default_color) # accessing class attribute via class

point.draw() 

another_point = Point(3, 4)

print(another_point.default_color) # accessing class attribute via another instance
another_point.draw()
# we can also define a class attribute and this are attributes we define at class level
# and they are the same across all the instances of the class
#e.g "as metaphore let's all humans has two eyes and two ears, and we define this attribute at class level all instances of that class will have this attributes"
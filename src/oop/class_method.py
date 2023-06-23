
#For Tutorial, refer to this link
#https://certifysphere.com/docs/tutorials/learn-python/object-oriented-programming/#class-methods

class Circle:
    PI = 3.14159  # Class-level attribute

    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_diameter(cls, diameter):
        radius = diameter / 2
        return cls(radius)

    def calculate_area(self):
        return self.PI * self.radius * self.radius

# Creating an instance using a class method
circle = Circle.from_diameter(10)

# Accessing instance attribute and invoking an instance method
print(circle.radius)  # Output: 5.0
print(circle.calculate_area())  # Output: 78.53975

#Run this program in terminal or command
#python3 class_method.py OR python class_method.py 
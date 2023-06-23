#For Tutorial, refer to this link
#https://certifysphere.com/docs/tutorials/learn-python/object-oriented-programming/#class-methods-and-instance-methods

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

# Creating instances of the Rectangle class
rectangle1 = Rectangle(5, 10)
rectangle2 = Rectangle(3, 6)

# Invoking the instance method on each instance
print(rectangle1.calculate_area())  # Output: 50
print(rectangle2.calculate_area())  # Output: 18

#Run this program in terminal or command
#python3 instance_method.py OR python instance_method.py
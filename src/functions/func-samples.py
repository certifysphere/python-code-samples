#https://certifysphere.com/docs/tuts/tutorials/learn-python/python-functions

#Example 1
def greet():
    print("Hello, world!")
# Calling the function
greet()  # Output: Hello, world!

#Example 2 -Functions can also accept parameters
def greet(name):
    print(f"Hello, {name}!")

# Calling the function with an argument
greet("Alice")  # Output: Hello, Alice!

#Example 3 - You can also specify default parameter values
def greet(name="world"):
    print(f"Hello, {name}!")

# Calling the function without providing an argument
greet()  # Output: Hello, world!

#Example 4 -  Functions can have multiple parameters
def add(a, b):
    return a + b

# Calling the function by position
result = add(2, 3)  # Output: 5
print(result)
# Calling the function by keyword
result = add(a=2, b=3)  # Output: 5
print(result)

#Example 5- variable-length arguments
def calculate_sum(*args):
    total = sum(args)
    return total

result = calculate_sum(1, 2, 3, 4, 5)  # Output: 15
print(result)


#Example 6- keyword arguments 
def calculate_product(a, b, c):
    product = a * b * c
    return product

result = calculate_product(a=2, b=3, c=4)  # Output: 24
print(result)

#To run this program in terminal or command, change directory to /src/functions and run the following command
# python func-samples.py
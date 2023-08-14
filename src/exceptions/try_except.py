#For Tutorial, refer to this link
#https://certifysphere.com/docs/tutorials/learn-python/working-with-files-and-input-output
#Example 1- The try-except Block
try:
    # Code that may raise an exception
    result = 10 / 0
except:
    # Code to handle the exception
    print("An error occurred!") #Output: An error occurred!

#Example 2 - Handling Specific Exceptions
try:
    # Code that may raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Code to handle the ZeroDivisionError
    print("Cannot divide by zero!") #Output: Cannot divide by zero!
except ValueError:
    # Code to handle the ValueError
    print("Invalid value!")

#Example 3-  else block
try:
    # Code that may raise an exception
    result = 10 / 2
except ZeroDivisionError:
    # Code to handle the ZeroDivisionError
    print("Cannot divide by zero!")
else:
    # Code to execute if no exceptions occur
    print("Result:", result) #Output: Result: 5.0

#Example 4 - The finally Block
try:
    # Code that may raise an exception
    result = 10 / 2
except ZeroDivisionError:
    # Code to handle the ZeroDivisionError
    print("Cannot divide by zero!")
finally:
    # Code to execute regardless of exceptions
    print("End of operation")     #Output: End of operation

#Example 5  - Raising Exceptions
try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative!")
except ValueError as e:
    print(str(e))
else:
    print(f"Entered age {age}")
#To run this program in terminal or command, change directory to /src/files and run the following command
#python3 try_except.py  OR python try_except.py 

#For Tutorial, refer to this link
#https://certifysphere.com/docs/tutorials/learn-python/working-with-files-and-input-output

# Reading a file
file_path = "example.txt"

# Method 1: Using the `open()` function and `read()` method
file = open(file_path, "r")
content = file.read()
file.close()
print(content)

# Method 2: Using the `with` statement (recommended)
with open(file_path, "r") as file:
    content = file.read()
    print(content)

#To run this program in terminal or command, change directory to /src/files and run the following command
#python3 reading_file.py OR python reading_file.py

#OUTPUT 
#Hello!!!! I am example file.
#Hello!!!! I am example file.

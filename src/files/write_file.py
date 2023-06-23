#For Tutorial, refer to this link
#https://certifysphere.com/docs/tutorials/learn-python/working-with-files-and-input-output

# Writing to a file
file_path = "output.txt"

# Method 1: Using the `open()` function and `write()` method
file = open(file_path, "w")
file.write("Hello, Python!")
file.close()

# Method 2: Using the `with` statement (recommended)
with open(file_path, "w") as file:
    file.write("Hello, Python!")

#To run this program in terminal or command, change directory to /src/files and run the following command
#python3  write_file.py OR python  write_file.py

#OUTPUT 
#It should create a new file "output.txt" in the current directory. Open file and check the contents.

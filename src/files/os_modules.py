#For Tutorial, refer to this link
#https://certifysphere.com/docs/tutorials/learn-python/working-with-files-and-input-output

import os

# Using functions from the os module
current_directory = os.getcwd()
print(current_directory)

file_exists = os.path.exists("myfile.txt")
print(file_exists)


#To run this program in terminal or command, change directory to /src/files and run the following command
#python3 os_modules.py OR python os_modules.py

#OUTPUT 
#it should print current directory and 'false' because myfile.txt does not exist. 
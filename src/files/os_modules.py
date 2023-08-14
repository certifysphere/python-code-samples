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

#import specific functions or classes from a module using the from keyword
from math import sqrt

result = sqrt(25)
print(result) # 5.0
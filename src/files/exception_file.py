#For Tutorial, refer to this link
#https://certifysphere.com/docs/tutorials/learn-python/working-with-files-and-input-output

# Exception handling
file_path = "nofile.txt"

try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found!")
except IOError:
    print("An error occurred while reading the file!")
except Exception as e:
    print(f"An error occurred: {str(e)}")

#To run this program in terminal or command, change directory to /src/files and run the following command
#python3 exception_file.py  OR python exception_file.py 

#OUTPUT 
#File not found!
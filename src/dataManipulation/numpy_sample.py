#https://certifysphere.com/docs/tuts/tutorials/learn-python/data-manipulation-and-analysis

# Example 1 - numpy
import numpy as np

# Create an array
arr = np.array([1, 2, 3, 4, 5])

# Perform computations
mean = np.mean(arr)
std_dev = np.std(arr)

print("Mean:", mean)
print("Standard Deviation:", std_dev)

#To run this program in terminal or command, change directory to /src/dataManipulation and run the following command
#python3 numpy_sample.py  OR python numpy_sample.py

#Output Mean: 3.0, Standard Deviation: 1.4142135623730951
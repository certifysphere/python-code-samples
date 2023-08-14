#https://certifysphere.com/docs/tuts/tutorials/learn-python/data-manipulation-and-analysis

import matplotlib.pyplot as plt

# Create data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create a line plot
plt.plot(x, y)

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot')

# Show the plot
plt.show()


#To run this program in terminal or command, change directory to /src/dataManipulation and run the following command
#python3 matplotlib_sample.py.py  OR python matplotlib_sample.py.py


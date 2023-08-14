#https://certifysphere.com/docs/tuts/tutorials/learn-python/data-manipulation-and-analysis
import pandas as pd

# Create a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Paris']
}

df = pd.DataFrame(data)

# Perform operations on the DataFrame
average_age = df['Age'].mean()
filtered_data = df[df['Age'] > 30]

print("Average Age:", average_age)
print("Filtered Data:")
print(filtered_data)

#To run this program in terminal or command, change directory to /src/dataManipulation and run the following command
#python3 pandas_sample.py OR python pandas_sample.py

#Output
# Average Age: 30.0
# Filtered Data:
#       Name  Age   City
# 2  Charlie   35  Paris
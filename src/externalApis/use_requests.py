#For Tutorial, refer to this link
#https://certifysphere.com/docs/tuts/tutorials/learn-python/working-with-external-libraries-and-apis

#Example 1 - Importing External Libraries
import requests
response = requests.get('https://openlibrary.org/api/books?bibkeys=ISBN:0201558025,LCCN:93005405&format=json')
print(response.status_code) # Output: 200 (if above api url is still up and running)

#Example 2 - Using APIs
data = response.json()

print(data) #Output: json response


#https://certifysphere.com/docs/tuts/tutorials/learn-python/web-scraping-with-python

# Example 1 - Requests and Beautiful Soup
import requests

url = 'https://www.example.com'
response = requests.get(url)
html_content = response.text

print(html_content)

#Example 2 - 
from bs4 import BeautifulSoup

# Assuming we have retrieved the HTML content in the variable 'html_content'
soup = BeautifulSoup(html_content, 'html.parser')

# Extracting data
title = soup.title.text
paragraphs = soup.find_all('p')

print("Title:", title)
print("Paragraphs:")
for p in paragraphs:
    print(p.text)
#To run this program in terminal or command, change directory to /src/webScraping and run the following command
#python3 requests_beautifulsoap.py OR python requests_beautifulsoap.py
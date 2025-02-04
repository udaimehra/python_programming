##
#Scraping Numbers from HTML using BeautifulSoup In this assignment you will write a Python program similar to http://www.py4e.com/code3/urllink2.py. The program will use urllib to read the HTML from the data files below, and parse the data, extracting numbers and compute the sum of the numbers in the file.
#
#We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.
#
#Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
#Actual data: http://py4e-data.dr-chuck.net/comments_2141807.html (Sum ends with 64)
#You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.
### Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
## Actual data: http://py4e-data.dr-chuck.net/comments_2141807.html (Sum ends with 64)
## 
# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file
# You are to find all the <span> tags in the file and pull out the numbers from the tag and sum the numbers.
import requests, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
containers = soup.findAll("span", {"class":"comments"})
sum=0
for line in containers:
    #print(line)
    ln=line.decode().split(">")
    ln1=ln[1].split("<")
    sum = sum+int(ln1[0])
    #print(ln1[0])
print(sum)
#table = soup.table
#print(soup.prettify())
#print(table)
#for ln in table:
#    print(ln)
# Retrieve all of the anchor tags
#tags = soup('a')
#for tag in tags:
#    print(tag.get('table', None))

##Ignore following lines
#for child in soup.descendants:
#    if child.name == "span":
#        print(soup.span.text)
    # Look at the parts of a tag
    #print('TAG:', tag)
    #print('URL:', tag.get('href', None))
    #print('Contents:', tag.contents[0])
    #print('Attrs:', tag.attrs)

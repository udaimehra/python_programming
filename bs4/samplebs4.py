# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

count=0
url = input('Enter - ')
markup = urlopen(url, context=ctx).read()
soup = BeautifulSoup(markup, "html.parser")
tbltag = soup.find('table')
rows = tbltag.find_all_next('span', {'class':'comments'})
for row in rows:
    count=count+1
    raw=str(row)
    raw_array=raw.split(">") 
    print(raw_array[1],count)
# Retrieve all of the anchor tags
tags = soup('table')
#for tag in tags:
#    # Look at the parts of a tag
#    print('TAG:', tag)
#    print('URL:', tag.get('span', None))
#    print('Contents:', tag.contents[0])
#    print('Attrs:', tag.attrs)

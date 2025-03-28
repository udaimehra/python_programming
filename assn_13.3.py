#Calling a JSON API

#In this assignment you will write a Python program somewhat 
#similar to http://www.py4e.com/code3/opengeo.py. The program 
#will prompt for a location, contact a web service and retrieve 
#JSON for the web service and parse that data, and retrieve the 
#first plus_code from the JSON. An Open Location Code is a textual 
#identifier that is another form of address based on the location 
#of the address.
#API End Points

#To complete this assignment, you should use this API endpoint 
#that has a static subset of the Open Street Map Data.

#http://py4e-data.dr-chuck.net/opengeo?
#This API also has no rate limit so you can test as often as you 
#like. If you visit the URL with no parameters, you get 
#"No address..." response.
#To call the API, you need to provide the address that you are 
#requesting as the q= parameter that is properly URL encoded 
#using the urllib.parse.urlencode() function as shown 
#in http://www.py4e.com/code3/opengeo.py

import urllib.request, urllib.parse
import json, ssl

# Heavily rate limited proxy of https://www.geoapify.com/ api
serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    address = address.strip()
    parms = dict()
    parms['q'] = address

    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'features' not in js:
        print('==== Download error ===')
        print(data)
        break

    if len(js['features']) == 0:
        print('==== Object not found ====')
        print(data)
        break

    # print(json.dumps(js, indent=4))

    #print(js['features'][0])
    pcode = js['features'][0]['properties']['plus_code']
    lat = js['features'][0]['properties']['lat']
    lon = js['features'][0]['properties']['lon']
    print('Plus code', pcode)
    #print('lat', lat, 'lon', lon)
    #location = js['features'][0]['properties']['formatted']
    #print(location)

import urllib.request, urllib.error, urllib.parse
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print("hello", line.decode().strip())
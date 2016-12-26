#!/usr/bin/python
import urllib2

url = raw_input("Enter http://")
response = urllib2.urlopen('http://%s:80/'%(url))
print 'RESPONSE:', response
print 'URL     :', response.geturl()

headers = response.info()
print 'DATE    :', headers['date']
print 'HEADERS :'
print '---------'
print headers

data = response.read()
print 'LENGTH  :', len(data)
print 'DATA    :'
print '---------'
print data

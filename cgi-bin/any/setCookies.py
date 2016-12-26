#!/usr/bin/python 
import requests
import time, Cookie 
# Instantiate a SimpleCookie object 
cookie = Cookie.SimpleCookie() 
# The SimpleCookie instance is a mapping 

cookie['lastvisit'] = str(time.time()) 
s = requests.session()
s.cookies.clear()
# Output the HTTP message containing the cookie 
print cookie 
print 'Content-Type: text/html\n' 
print '<html><body>' 
print 'Server time is', time.asctime(time.localtime()) 
print '</body></html>'
#!/usr/bin/python 
import requests
import time, Cookie 
import cgi,cgitb
# Instantiate a SimpleCookie object 
cookie = Cookie.SimpleCookie() 
# The SimpleCookie instance is a mapping 
cookie['login'] = ''
cookie['login']['expires']='0'
s = requests.session()
s.cookies.clear()
# Output the HTTP message containing the cookie 
print cookie 
print 'Content-Type: text/html\n' 
print '<html><head>' 
homeIP = '192.168.0.102'
print ('''<meta http-equiv="refresh" content="0.1;http://%s">'''%(homeIP))
print '</head></html>'
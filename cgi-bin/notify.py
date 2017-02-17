#!/usr/bin/python 
# -*- coding: utf-8 -*-f
import requests,json
from urlparse import urlparse
import urllib
#Import modules for CGI handling  
import cgi, cgitb
import Cookie, os, time 

cookie = Cookie.SimpleCookie() 
cookie_string = os.environ.get('HTTP_COOKIE') 
# Create instance of FieldStorage  
form = cgi.FieldStorage()  
# Get data from fields
data_input = form.getvalue('data')
api_key = form.getvalue('key')

def getCookies():
    if not cookie_string:
        return False
    else:
        # load() parses the cookie string
        cookie.load(cookie_string)
        # Use the value attribute of the cookie to get it 
        txt = str(cookie['login'].value)
        if txt == 'success':
            return True
        else:
            return False

def verify():
  if api_key == 'abcd':
    return True
  else:
    return False

def check_login():
	if (verify() or getCookies()):
		return True
	else:
		return False
            
if check_login() == False:
	print 'Content-Type: text/html\n' 
	print '<html><head>' 
	homeIP = 'siczones.coe.psu.ac.th'
	print ('''<meta http-equiv="refresh" content="0.1;http://%s">'''%(homeIP))
	print '</head></html>'
else:
	LINE_ACCESS_TOKEN="P8xV9pSkPz5NRedG3GL45TDKDTVmnqx402fedP8IHs8"
	url = "https://notify-api.line.me/api/notify"

	message = data_input 

	msg = urllib.urlencode(({"message":message}))
	LINE_HEADERS = {'Content-Type':'application/x-www-form-urlencoded',"Authorization":"Bearer "+LINE_ACCESS_TOKEN}
	session = requests.Session()
	a=session.post(url, headers=LINE_HEADERS, data=msg)

	print("Content-type: text/html") 
	print("")  
	print("<html><head>") 
	print("""
		<title>LINE notify</title>
		<meta charset="utf-8">
		<link href="../favicon.ico" rel="icon" type="image/x-icon"/>     
		<link href="../favicon.ico" rel="shortcut icon" type="image/x-icon"/>
		<!-- This file has been downloaded from Bootsnipp.com. Enjoy! -->
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<link href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.0/css/bootstrap.min.css" rel="stylesheet">

		<!-- Custom Fonts -->
		<link href="/vendor/font-awesome/css/font-awesome.min.css" rel="stylesheet" type="text/css">
		<link href="https://fonts.googleapis.com/css?family=Montserrat:400,700" rel="stylesheet" type="text/css">
		<link href='https://fonts.googleapis.com/css?family=Kaushan+Script' rel='stylesheet' type='text/css'>
		<link href='https://fonts.googleapis.com/css?family=Droid+Serif:400,700,400italic,700italic' rel='stylesheet' type='text/css'>
		<link href='https://fonts.googleapis.com/css?family=Roboto+Slab:400,100,300,700' rel='stylesheet' type='text/css'>

		<!-- Theme CSS -->
		<link href="../css/agency.css" rel="stylesheet">
		<link href="../css/siczones.css" rel="stylesheet">

		<script src="http://code.jquery.com/jquery-1.11.1.min.js"></script>
		<script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.0/js/bootstrap.min.js"></script>
	""") 
	print("</head><body>") 
	print("<h2>OK </h2>")
	print("<h4>Message : %s </h4>" %data_input)
	print('''<br><br><a href="javascript:window.close();">Close ปิด</a> ''')
	# print(a.text)
	print("</body></html>") 

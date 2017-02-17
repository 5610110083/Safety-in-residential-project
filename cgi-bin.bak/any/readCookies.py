#!/usr/bin/python 
import Cookie, os, time 
cookie = Cookie.SimpleCookie() 
print 'Content-Type: text/html\n' 
print '<html><body>' 
# The returned cookie is available in the os.environ dictionary 
cookie_string = os.environ.get('HTTP_COOKIE') 
# The first time the page is run there will be no cookies 
if not cookie_string: 
	print '<p>First visit or cookies disabled</p>' 
else: # Run the page twice to retrieve the cookie 
    print '<p>The returned cookie string was "' + cookie_string + '"</p>' 
   # load() parses the cookie string 
    cookie.load(cookie_string) 
   # Use the value attribute of the cookie to get it 
    lastvisit = float(cookie['lastvisit'].value) 
    print '<p>Your last visit was at', 
    print time.asctime(time.localtime(lastvisit)), '</p>' 
print '</body></html>' 
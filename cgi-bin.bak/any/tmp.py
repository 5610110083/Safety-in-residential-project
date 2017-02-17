#!/usr/bin/python

print 'Content-Type: text/html\r\n'
print 'Set-Cookie: raspberrypi="Hello world";expires=Sat Jul 09 23:43:31 2016 GMT \r\n\r\n'

print """
<html>
    <body>
        <h1>Some web page</h1>
    </body>
</html>
"""
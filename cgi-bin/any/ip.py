#!/usr/bin/python 
import cgi
import os

print "Content-type: text/html"
print ""
try:
	print cgi.escape(os.environ["REMOTE_ADDR"])
except:
	pass

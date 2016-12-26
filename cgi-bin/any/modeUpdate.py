#!/usr/bin/python 
import ConfigParser
import cgi, cgitb
import Cookie, os, time 

# Update MODE
def writeMode(value):
  section = 'MODE'
  confName = 'mode'
  config= ConfigParser.RawConfigParser()
  config.read(r'setting\config.ini')
  config.set(section,confName,value )
  with open(r'setting\config.ini', 'wb') as configfile:
      config.write(configfile)

#read mode from get method and config
cgitb.enable()
form=cgi.FieldStorage()
if "currentMode" not in form:
  #print 'data not input'
  pass
else:
  modeVal=form["currentMode"].value
  writeMode(modeVal)

print "Content-type: text/html\n\n"
print "<b>success</b>"

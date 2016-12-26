#!/usr/bin/python 
#!/usr/bin/python 
import ConfigParser
import cgi, cgitb
import Cookie, os, time 

cgitb.enable()
form=cgi.FieldStorage()

if "value" not in form:
	value=0
else:
	value=form["value"].value

# Update MODE
section = 'MODE'
confName = 'mode'
config= ConfigParser.RawConfigParser()
config.read(r'setting\config.ini')
config.set(section,confName,value )
with open(r'setting\config.ini', 'wb') as configfile:
    config.write(configfile)

print "Content-type: text/html\n\n"
print ("<h1>Success mode: %s >> active <<</h1>"%(value)) 


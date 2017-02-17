#!/usr/bin/python 
import ConfigParser
import cgi, cgitb
import Cookie, os, time 

'''
Config = ConfigParser.ConfigParser()
cfgfile = open("setting\config.ini",'w') # a+ is append or update Mode
# add the settings to the structure of the file, and lets write it out...
Config.add_section('MODE')
Config.set('MODE','off', '0')
Config.set('MODE','basic', '0')
Config.set('MODE','full', '0')
Config.set('MODE','advance', '0')

# add the settings to the structure of the file, and lets write it out...
Config.add_section('LINE')
Config.set('LINE','USERNAME', 'sic@outlook.co.th')
Config.set('LINE','PASSWORD', '1234567896')
Config.set('LINE','GROUPNAME', 'Line-bot')
Config.write(cfgfile)
cfgfile.close()
'''

# Update LINE
section = 'LINE'
confName = 'username'
value = 'sic@outlook.co.thhhh'
config= ConfigParser.RawConfigParser()
config.read(r'setting\config.ini')
config.set(section,confName,value )
with open(r'setting\config.ini', 'wb') as configfile:
    config.write(configfile)
'''


'''
# Update MODE
section = 'MODE'
confName = 'off'
value = '3'
config= ConfigParser.RawConfigParser()
config.read(r'setting\config.ini')
config.set(section,confName,value )
with open(r'setting\config.ini', 'wb') as configfile:
    config.write(configfile)


cgitb.enable()
form=cgi.FieldStorage()

print "Content-type: text/html\n\n"
if "data" not in form:
    print "<h1>The text input box was empty.</h1>"
else:
    text=form["data"].value
    print "<h1>Text from text input box:</h1>"
    print cgi.escape(text)
    


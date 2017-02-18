#!/usr/bin/python 
# -*- coding: utf-8 -*-f
import json
import httplib, urllib, urllib2
import time
from datetime import datetime

import requests
import urllib
#!/usr/bin/python 
# -*- coding: utf-8 -*-f
#Import modules for CGI handling  
import cgi, cgitb
import Cookie, os, time 
#============================ config mode ===================== #
import ConfigParser

#Import modules for CGI handling  
import cgi, cgitb

# Create instance of FieldStorage
form = cgi.FieldStorage() 
humidity = form.getvalue('humidity')
temperature = form.getvalue('temperature')
soilmoisture = form.getvalue('soilmoisture')


Config = ConfigParser.ConfigParser()
setting = Config.read('setting/config.ini')
settingSec = Config.sections()
#print settingSec

def ConfigSectionMap(section):
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1

#Reading config mode
def readMode():
  try:
    MODE = ConfigSectionMap('MODE')
    return MODE['mode']
  except:
    print 'Data not found.'
    return 0

# Update config MODE
def writeTemp(value):
  # lets create that config file for next time...
  cfgfile = open("setting/config.ini",'wb')
  # add update the settings to the structure of the file, and lets write it out...
  Config.set('DATA','temperature', value)
  Config.write(cfgfile)
  cfgfile.close()
  
def writeHumid(value):
  # lets create that config file for next time...
  cfgfile = open("setting/config.ini",'wb')
  # add update the settings to the structure of the file, and lets write it out...
  Config.set('DATA','humidity', value)
  Config.write(cfgfile)
  cfgfile.close()
  
def writeSoil(value):
  # lets create that config file for next time...
  cfgfile = open("setting/config.ini",'wb')
  # add update the settings to the structure of the file, and lets write it out...
  Config.set('DATA','soilmoisture', value)
  Config.write(cfgfile)
  cfgfile.close()
  
writeHumid(humidity)
writeTemp(temperature)
writeSoil(soilmoisture)
#url = 'https://esptemp-144510.appspot.com/_ah/api/sensorrecord/v1/record?fields=humidity'
payload = {"humidity": humidity,
			"temperature": temperature,
			"soilmoisture": soilmoisture }

req = urllib2.Request('https://esptemp-144510.appspot.com/_ah/api/sensorrecord/v1/record?fields=humidity')
req.add_header('Content-Type', 'application/json')
response = urllib2.urlopen(req, json.dumps(payload))
#print payload
#try:
	#r = request.post(url, json={"humidity": humidity})
	#print r
#except:
	#print 'connect failed'
	#pass

print 'content-type:  application/json\n' 
print 'Content-Type: text/html\n' 
print '<html><head>'
print humidity
print '<br>'
print temperature
print '<br>'
print soilmoisture
print '<br>'
print '</head></html>'

#!/usr/bin/python
# This program logs a Raspberry Pi's CPU temperature to a Thingspeak Channel
# To use, get a Thingspeak.com account, set up a channel, and capture the Channel Key at https://thingspeak.com/docs/tutorials/ 
# Then paste your channel ID in the code for the value of "key" below.
# Then run as sudo python pitemp.py (access to the CPU temp requires sudo access)
# Author : siczones

import httplib, urllib
import time
from datetime import datetime

#Import modules for CGI handling  
import cgi, cgitb


############ Upload to clound #################
sleep = 20 # how many seconds to sleep between posts to the channel (at least 20 second)
key = '9227DXSLR71NKKMO'  # Thingspeak channel to update
#initial status
Active = 1
Alert = 0
Humidity = 0
Voice = 0
Light = 0
Fire = 0
Temp = 0

#Report Raspberry Pi internal temperature to Thingspeak Channel
def uploadThingSpeak(data,numField):
        while True:
                params = urllib.urlencode({('field%d'%(numField)): data, 'key':key }) 
                headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
                conn = httplib.HTTPConnection("api.thingspeak.com:80")
                try:
                        conn.request("POST", "/update", params, headers)
                        response = conn.getresponse()
                        #print ('Field%s : %s' %(numField, data))
                        #print response.status #if show 200 is success
                        print 'Status :',response.reason
                        data = response.read()
                        conn.close()
                except:
                        print "connection failed"
                break
'''
def updateData():
    global Active,Alert,Humidity,Voice ,Light,Fire,Temp

    #Calculate CPU temperature of Raspberry Pi in Degrees C
    temp = int(open('/sys/class/thermal/thermal_zone0/temp').read()) / 1e3 # Get Raspberry Pi CPU temp
    Active = temp
    Alert = 2
    Humidity = 3
    Voice = 4
    Light = 5
    Fire = 6
    Temp = 7
    #print ('updateData Active')


if __name__ == "__main__":
    #while True:
    print '=============================='
    #Show time
    print datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    updateData()
    fields = [Active,Alert,Humidity,Voice,Light,Fire,Temp]
    numField = 1
    for data in fields:
        uploadThingSpeak(data,numField)
        numField = numField+1
'''

############################### HTML ##########################
# Create instance of FieldStorage  
form = cgi.FieldStorage()  

print ("Content-type:text/html\r\n\r\n") 
print ("<html>")
print ("<head>") 
print ("<title>UploadThingSpeak</title>") 
print ("</head>") 
print ("<body>")
print ("<center><fieldset><legend>Result !!</legend>")
print ("<h2>Welcome to Upload data to ThingSpeak</h2>")

i=1
Field=[]
while i<=7 :
        # Get data from fields 
        Field.append(form.getvalue('Field%s'%(i)))
        print ("<p>Field%s : %s" % (i,Field[i-1]))
        if Field[i-1] is not None:
                uploadThingSpeak(Field[i-1],i)
                if (form.getvalue('Field%s'%(i+1)) is not None):
                #sleep for desired amount of time
                        time.sleep(sleep)
        i=i+1
	
print ('''<FORM><INPUT Type="button" VALUE="Back" onClick="history.go(-1);return true;"></FORM>''')
print ("</fieldset></center></body>") 
print ("</html>")


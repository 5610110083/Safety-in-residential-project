#!/usr/bin/env python
# This program logs a Raspberry Pi's CPU temperature to a Thingspeak Channel
# To use, get a Thingspeak.com account, set up a channel, and capture the Channel Key at https://thingspeak.com/docs/tutorials/ 
# Then paste your channel ID in the code for the value of "key" below.
# Then run as sudo python pitemp.py (access to the CPU temp requires sudo access)
# Author : siczones

import httplib, urllib
import time
from datetime import datetime
import pigpio
import requests
import urllib

sleep = 120 # how many seconds to sleep between posts to the channel (at least 15 second)

#Report Raspberry Pi internal temperature to apache webserver
def sent_data(value):
    # Login
    url = 'http://siczones.coe.psu.ac.th/cgi-bin/UploadThingSpeakWithSensor.py'
    values = {'key': 'abcd',
              'Field1': value}
    try:
        r = requests.post(url, data=values)
        #print r.content
        print '    Report to webserver success'
    except:
        print '    Report to webserver failed.'
########################################################################
    
def autoFan(temp):
    x = float(temp)   
    if (x > 33.0):
        pin=21
        pi = pigpio.pi() # Connect to local Pi.
        pi.set_mode(pin, pigpio.OUTPUT)
        for i in range(10):
            pi.write(pin, 0)
        pi.stop()
    else:
        pin=21
        pi = pigpio.pi() # Connect to local Pi.
        pi.set_mode(pin, pigpio.OUTPUT)
        for i in range(10):
            pi.write(pin, 1)
        pi.stop()
    
    
if __name__ == "__main__":
    while True:
        #Calculate CPU temperature of Raspberry Pi in Degrees C
        temp = int(open('/sys/class/thermal/thermal_zone0/temp').read()) / 1e3 # Get Raspberry Pi CPU temp
        
        print '=========================================================================='
        print '*** Welcome to RPi Temp report to cloud and auto on/off fan V.1.1'
        print '*** Powered by siczones'
        print ''        
        #Show time
        print '*** Date :' + datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print '*** Please enter <Ctrl+C> to skip this and continue to go to terminal.'
        print "\n    Temperature :\t"+str(temp) + " *C"
        sent_data(temp)
        autoFan(temp) 
        print '=========================================================================='               
        time.sleep(sleep)
        
        
        

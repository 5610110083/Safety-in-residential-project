#!/usr/bin/python 
# -*- coding: utf-8 -*-f
# This program logs a Raspberry Pi's CPU temperature to a Thingspeak Channel
# Help: ?
# This program accept to use from key="abcd" in url request , When this sensor request link from get method to server.
# The server will processing and use check alert function and notify to LINE when humindity to lower than rule and other field to higher than rule.
# Author : siczones 

import httplib, urllib
import time
from datetime import datetime

import requests
import urllib

#Import modules for CGI handling  
import cgi, cgitb

#=====================***** C-o-n-f-i-g--m-o-d-e *****================ #
import ConfigParser

Config = ConfigParser.ConfigParser()
Config.read(r'setting/devices.ini')
settingSec = Config.sections()
#print settingSec

def ConfigSectionMap(device_No):
    dict1 = {}
    options = Config.options(device_No)
    for option in options:
        try:
            dict1[option] = Config.get(device_No, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1

#==============Reading config of device=============

def getAmount():
	try:
		amountDevice = ConfigSectionMap('NumDevice')
		return amountDevice['amount']
	except:
		print 'Data not found.'
		return 0
		
def getName(device_No):
	try:
		Device = ConfigSectionMap('Device'+str(device_No))
		return Device['name']
	except:
		return 'Data not found.'
		
def getAPI_key(device_No):
	try:
		Device = ConfigSectionMap('Device'+str(device_No))
		return Device['api-key']
	except:
		return 'Data not found.'

def getAlert_type(device_No):
	try:
		Device = ConfigSectionMap('Device'+str(device_No))
		return Device['alert_type']
	except:
		return 'Data not found.'

def getDecision_point(device_No):
	try:
		Device = ConfigSectionMap('Device'+str(device_No))
		return Device['decision_point']
	except:
		return 'Data not found.'
		
#============== End Reading config of device =============
 
# Create instance of FieldStorage
form = cgi.FieldStorage() 

#======================= Verify device =======================#
#generate apiKey for verify sensor device access
apiKey = form.getvalue('key')
def verify():
  if apiKey == 'abcd':
    return True
  else:
    return False
#==================== End Verify device =====================#   

#===================== Upload to clound ======================#
# This time to sleep between posts to the channel(at least 20second)
sleep = 15
# API Key Thingspeak channel to update
key = '9227DXSLR71NKKMO'
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
                return
#===================== End Upload to clound ======================#   

#===================== AlertCheck ======================#  
#set rule alert
RPi_temp = 50.0
Alert = 0.0
Humidity = 10.0
Voice = float(getDecision_point(2))
Light = float(getDecision_point(3))
Home_Temp = float(getDecision_point(1))
Motion = float(getDecision_point(4))
fieldName = ['RPi_temp','Alert','Humidity','Voice','Light','Home_Temp','Motion']
rule = [RPi_temp,Alert,Humidity,Voice,Light,Home_Temp,Motion]

def line_notify(data_value):
	#### Alert to web
	link = "http://siczones.coe.psu.ac.th/cgi-bin/notify.py?key=abcd&data="
	link = link + data_value
	f = urllib.urlopen(link)

#Uncomment to test
#line_notify('1')
def alertCheck(data,numField):
	if int(numField) == 3:
		## if Humidity low let alert
		if data < rule[numField-1]:
			#print '################### Alert Active ####################'
			uploadThingSpeak(numField,2) ## show alert graph is alert from from field 3
			# logCreate(data,numField)
			#print ('''<meta http-equiv="refresh" content="0.1;http://siczones.coe.psu.ac.th/cgi-bin/notify.py?data=%s">'''%(fieldName[numField-1]))

			#### Alert to web
			line_notify(fieldName[numField-1]+": "+str(data))
	elif int(numField) == 4:
		## if Humidity low let alert
		if data > rule[numField-1]:
			#print '################### Alert Active ####################'
			uploadThingSpeak(numField,2) ## show alert graph is alert from from field 3
			# logCreate(data,numField)
			#print ('''<meta http-equiv="refresh" content="0.1;http://siczones.coe.psu.ac.th/cgi-bin/notify.py?data=%s">'''%(fieldName[numField-1]))

			#### Alert to web
			line_notify(fieldName[numField-1]+": "+ "มีเสียงพูด")
	else:
		## other field higher than rule let alert
		if data > rule[numField-1]:
			print ('################### Field%s : Alert Active ###################'%(numField))
			uploadThingSpeak(numField,2) ## show alert graph is alert from from numfield 
			#print ('''<meta http-equiv="refresh" content="0.1;http://siczones.coe.psu.ac.th/cgi-bin/notify.py?data=%s">'''%(fieldName[numField-1]))
			#logCreate(data,numField)

			#### Alert to web
			line_notify(fieldName[numField-1]+": "+str(data))
			
#### Alert to web
#a = form.getvalue('Field7')
#line_notify(str(a))

## Uncomment test LINE alert
#alertCheck(50,7)

#===================== End alertCheck ======================#
#===================== Start logCreate ======================#
def logCreate(data,numField):
  #print file
  with open("../logfiles/alert.log", "a") as text_file:
    text_file.write("\r%s > Field%s: %s" %(time.ctime(), (numField),(data) ))
    return
##Uncomment test LINE alert
#logCreate(105,7)
#===================== End logCreate ======================#
#========================== HTML ===========================#
if verify() is False:
  print 'Content-Type: text/html\n' 
  print '<html><head>'
  homeIP = 'siczones.coe.psu.ac.th'
  print ('''<meta http-equiv="refresh" content="0.1;http://%s">'''%(homeIP))
  print '</head></html>'
else:
  print ("Content-type:text/html\r\n\r\n") 
  print ('''<!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="utf-8">
      <!-- This file has been downloaded from Bootsnipp.com. Enjoy! -->
      <title>UploadThingSpeak</title>
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <link href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.0/css/bootstrap.min.css" rel="stylesheet">
      <link href="../favicon.ico" rel="icon" type="image/x-icon"/>     
      <link href="../favicon.ico" rel="shortcut icon" type="image/x-icon"/>
      <style type="text/css">
  .wrapper {    
    margin-top: 20px;
    margin-bottom: 20px;
  }

  .form-signin {
    max-width: 820px;
    padding: 20px 50px 20px;
    margin: 0 auto;
    border: 3px dotted rgba(0,0,0,0.1);  
    }

  .form-signin-heading {
    text-align:center;
    margin-bottom: 30px;
  }

  .form-control {
    position: relative;
    font-size: 16px;
    height: auto;
    padding: 10px;
  }

  input[type="text"] {
    margin-bottom: 0px;
    border-bottom-left-radius: 0;
    border-bottom-right-radius: 0;
  }

  input[type="password"] {
    margin-bottom: 20px;
    border-top-left-radius: 0;
    border-top-right-radius: 0;
  }

  .colorgraph {
    height: 7px;
    border-top: 0;
    background: #c4e17f;
    border-radius: 5px;
    background-image: -webkit-linear-gradient(left, #c4e17f, #c4e17f 12.5%, #f7fdca 12.5%, #f7fdca 25%, #fecf71 25%, #fecf71 37.5%, #f0776c 37.5%, #f0776c 50%, #db9dbe 50%, #db9dbe 62.5%, #c49cde 62.5%, #c49cde 75%, #669ae1 75%, #669ae1 87.5%, #62c2e4 87.5%, #62c2e4);
    background-image: -moz-linear-gradient(left, #c4e17f, #c4e17f 12.5%, #f7fdca 12.5%, #f7fdca 25%, #fecf71 25%, #fecf71 37.5%, #f0776c 37.5%, #f0776c 50%, #db9dbe 50%, #db9dbe 62.5%, #c49cde 62.5%, #c49cde 75%, #669ae1 75%, #669ae1 87.5%, #62c2e4 87.5%, #62c2e4);
    background-image: -o-linear-gradient(left, #c4e17f, #c4e17f 12.5%, #f7fdca 12.5%, #f7fdca 25%, #fecf71 25%, #fecf71 37.5%, #f0776c 37.5%, #f0776c 50%, #db9dbe 50%, #db9dbe 62.5%, #c49cde 62.5%, #c49cde 75%, #669ae1 75%, #669ae1 87.5%, #62c2e4 87.5%, #62c2e4);
    background-image: linear-gradient(to right, #c4e17f, #c4e17f 12.5%, #f7fdca 12.5%, #f7fdca 25%, #fecf71 25%, #fecf71 37.5%, #f0776c 37.5%, #f0776c 50%, #db9dbe 50%, #db9dbe 62.5%, #c49cde 62.5%, #c49cde 75%, #669ae1 75%, #669ae1 87.5%, #62c2e4 87.5%, #62c2e4);
  }

  .btn-form {
    position: relative;
    margin-bottom: 5px;
  }

  .back-to-top {
    cursor: pointer;
    position: fixed;
    bottom: 20px;
    right: 20px;
    display:none;
  }
      </style>
      <script src="http://code.jquery.com/jquery-1.11.1.min.js"></script>
      <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.0/js/bootstrap.min.js"></script>
      <script>
    $(document).ready(function(){
       $(window).scroll(function () {
              if ($(this).scrollTop() > 50) {
                  $('#back-to-top').fadeIn();
              } else {
                  $('#back-to-top').fadeOut();
              }
          });
          // scroll body to 0px on click
          $('#back-to-top').click(function () {
              $('#back-to-top').tooltip('hide');
              $('body,html').animate({
                  scrollTop: 0
              }, 800);
              return false;
          });
          
          $('#back-to-top').tooltip('show');

  });
  </script>

  </head>''') 
  print ('''
  <body>
      <div class = "container">
      <div class="wrapper">
  <center><fieldset>
  <h3 class="form-signin-heading">Welcome to Upload data to ThingSpeak</h3>
  <hr class="colorgraph"><div class="form-signin">''')

  i=1 
  Field=[]
  while i<=8 :
          # Get data from fields 
          try:
          	Field.append(form.getvalue('Field%s'%(i)))
          except:
          	pass
          print ('''<p class="form-control">Field%s : %s''' % (i,Field[i-1]))
          if Field[i-1] is not None:
                  uploadThingSpeak(float(Field[i-1]),i)
                  #print alert to log file
                  logCreate(Field[i-1],i)
                  
                  #uncomment print output to file
                  #with open("alert.log", "a") as text_file:
                  #  text_file.write("%s >>>>> Field%s : %s\n" %(time.ctime(),i,Field[i-1]))
                  
                  #check alert and alert to LINE
                  alertCheck(float(Field[i-1]),i)
                  
                  #line_notify(Field[i-1])
                  
                  #if had more than one field.let use sleep time Please Uncomment
                  # if (form.getvalue('Field%s'%(i+1)) is not None):
                  #   #sleep for desired amount of time
                  #   time.sleep(sleep)
                  #   pass
          i=i+1
    
  print ('''</div><br>
          <FORM action="status.py" class="btn-form"><button class="btn btn-lg btn-success btn-block" Type="submit" VALUE="Status" onmouseover="style.color='yellow'" onmouseout="style.color='white'">Status</button></FORM>
          <FORM class="btn-from"><button class="btn btn-lg btn-primary btn-block" Type="button" VALUE="Back" onClick="history.go(-1);return true;">Back</button></FORM>''')
  print ('''</fieldset></center></div></div>
    <br/>
  <!-- ============== Footer ============ -->
    <br/><br/><div class="navbar navbar-default navbar-fixed-bottom">
      <div class="container">
        <p class="navbar-text pull-left">Copyright 2016-2017 Siczones.</p>
        <!-- a id="back-to-top" href="#" class="navbar-btn btn-danger btn pull-right" role="button" data-toggle="tooltip" data-placement="left"><span class="glyphicon glyphicon-chevron-up"></span></a -->

        <!-- Split button -->
        <div class="navbar-btn btn-group dropup pull-right">
          <button id="back-to-top" href="#" type="button" class="btn btn-warning"><span class="glyphicon glyphicon-chevron-up"></span> Top</button>
        </div>
      </div>  
  </div>
  <!-- ============== End Footer ============ -->
    </body>''') 
  print ("</html>")
  exit()
  print("============================================================================")
  print("==================== = = = ==  S u c c e s s  == = = = =====================")
  print("============================================================================")

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
#Import line
from line import LineClient, LineGroup, LineContact
import Cookie, os, time 
cookie = Cookie.SimpleCookie() 
cookie_string = os.environ.get('HTTP_COOKIE') 
def getCookies():
    if not cookie_string: 
        return False
    else:
        # load() parses the cookie string
        cookie.load(cookie_string)
        # Use the value attribute of the cookie to get it 
        txt = str(cookie['login'].value)
        if txt == 'success':
            return True
        else:
            return False
            
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
#===================== Upload to clound ======================#       
#===================== Start LINE ALERT ======================#
loginLine = False
def lineAlert(MSG,nField):
        USERNAME = 'sic@outlook.co.th'
        PASSWORD = '1234567896'
        GROUPNAME = 'Line-bot'
        #MSG = 'hello world!'
        #optional
        COMPUTERNEME = 'Siczones.Bot'
        TOKEN = ''
        global loginLine
        while loginLine is False:
                try:
                        client = LineClient(id=USERNAME, password=PASSWORD, authToken=TOKEN, com_name=COMPUTERNEME)
                        TOKEN = client.authToken
                        #print "TOKEN : %s\r\n" % TOKEN
                        client_group = client.getGroupByName(GROUPNAME)
                        #print client_group
                        loginLine = True
                        print "Login success"
                except:
                        print "Login Failed"

        if loginLine is True:
                try:
                        by = "[Webpage bot]"
                        client_group.sendMessage("Fielld :%s \n %s" % ( nField,MSG, by))
                        return
                except:
                        #print 'sender failed'
                        lineAlert(MSG,nField)

#===================== END LINE ALERT ======================#
#========================== HTML ===========================#
# Create instance of FieldStorage

form = cgi.FieldStorage()  
if getCookies() == False:
  print 'Content-Type: text/html\n' 
  print '<html><head>' 
  homeIP = '192.168.0.102'
  print ('''<meta http-equiv="refresh" content="0.1;http://%s">'''%(homeIP))
  print '</head></html>'
else:
  print ("Content-type:text/html\r\n\r\n") 
  print ('''<!DOCTYPE html>
  <html lang="en">
<head>
<title>Upload ThingSpeak</title>
<meta charset="utf-8">
<link href="../favicon.ico" rel="icon" type="image/x-icon"/>     
<link href="../favicon.ico" rel="shortcut icon" type="image/x-icon"/>
<!-- This file has been downloaded from Bootsnipp.com. Enjoy! -->
<meta name="viewport" content="width=device-width, initial-scale=1">
<link href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.0/css/bootstrap.min.css" rel="stylesheet">

    <!-- Theme CSS -->
    <link href="/css/agency.min.css" rel="stylesheet">
    <link href="/css/siczones.css" rel="stylesheet">

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
     <!-- ==================== Nav Tabs ======================= -->
      <nav class="nav nav-tabs navbar-inverse navbar-fixed-top">
        <div class = "container">
        <ul class="nav nav-tabs">
          <li role="presentation"><a href="index.py">Home</a></li>
          <li role="presentation" ><a href="mode.py">Mode</a></li>
          <li role="presentation" class="dropdown active">
            <a class="dropdown-toggle" data-toggle="dropdown" href="#" role="button" aria-haspopup="true" aria-expanded="false">
              Other<span class="caret"></span>
            </a>
                <ul class="dropdown-menu">
                  <li><a href="status.py">Status</a></li>
                  <li><a href="device.py">Device</a></li>
                  <li><a href="alert.py">Alert</a></li>
                  <li role="separator" class="divider"></li>
                  <li><a href="logout.py" onmouseover="style.color='red'" onmouseout="style.color='black'">Log out</a></li>
                </ul>
          </li>
        </ul>
        </div>
      </nav>
      <br/><br/>
      <div class="container-fluid" id="grad1">
        <div class="container">
        <div class="navbar-header">
          <h2 class="class="section-subheading text-muted"">
            <a class="navbar-brand">Safety in residential system </a>
          </h2>    
        </div>
        </div>
      </div>
      <!-- ========================== Nav Tabs ======================= -->
      <div class = "container">
      <div class="wrapper">
  <center><fieldset><legend>Result !!</legend>
  <h3 class="form-signin-heading">Welcome to Upload data to ThingSpeak</h3>
  <hr class="colorgraph"><div class="form-signin">''')
  i=1
  count = False
  while i<=7 : 
          if (form.getvalue('Field%s'%(i))):
            count = True
            break
          i = i+1
  if count is True:
    print('''<div class="alert alert-success" role="alert">Receive data value success !</div>''')
  else:
    print('''<div class="alert alert-warning" role="alert">No data value !</div>''')
  i=1 
  Field=[]
  while i<=7 :
          # Get data from fields 
          Field.append(form.getvalue('Field%s'%(i)))
          print ('''<p class="form-control">Field%s : %s''' % (i,Field[i-1]))
          if Field[i-1] is not None:
                  uploadThingSpeak(float(Field[i-1]),i)
                  #if had more than one field then use sleep time
                  if (form.getvalue('Field%s'%(i+1)) is not None):
                          #sleep for desired amount of time
                          time.sleep(sleep)
          i=i+1
  	
  print ('''</div><br>
          <FORM action="status.py" class="btn-form"><button class="btn btn-lg btn-success btn-block" Type="submit" VALUE="Status" onmouseover="style.color='yellow'" onmouseout="style.color='white'">Status</button></FORM>
          <FORM class="btn-from"><button class="btn btn-lg btn-primary btn-block" Type="button" VALUE="Back" onClick="history.go(-1);return true;">Back</button></FORM>''')
  print ('''</fieldset></center></div></div>
  	<br/><br/>
  <!-- ============== Footer ============ -->
    <br/><br/><div class="navbar navbar-default navbar-fixed-bottom">
      <div class="container">
        <p class="navbar-text pull-left">Copyright <span class="glyphicon glyphicon-copyright-mark"> </span> 2016 - Siczones.</p>
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
  '''
  i=1
  while i<=7 :
          if Field[i-1] is not None:
                  lineAlert( str(Field[i-1]), str(i))
          i = i+1
  '''
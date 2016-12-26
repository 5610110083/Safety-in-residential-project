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

############ Upload to clound #################
sleep = 20 # how many seconds to sleep between posts to the channel (at least 20 second)
key = '9227DXSLR71NKKMO'  # Thingspeak channel to update

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

############################### HTML ##########################
# Create instance of FieldStorage  
form = cgi.FieldStorage()  

if getCookies() == False:
  print 'Content-Type: text/html\n' 
  print '<html><head>' 
  homeIP = '172.30.142.209'
  print ('''<meta http-equiv="refresh" content="0.1;http://%s">'''%(homeIP))
  print '</head></html>'
else:
  print ("Content-type:text/html\r\n\r\n") 
  print ('''<!DOCTYPE html>
  <html lang="en">
<head>
<title>Status</title>
<meta charset="utf-8">
<link href="../favicon.ico" rel="icon" type="image/x-icon"/>     
<link href="../favicon.ico" rel="shortcut icon" type="image/x-icon"/>
<!-- This file has been downloaded from Bootsnipp.com. Enjoy! -->
<meta name="viewport" content="width=device-width, initial-scale=1">
<link href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.0/css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom Fonts -->
    <link href="/vendor/font-awesome/css/font-awesome.min.css" rel="stylesheet" type="text/css">
    <link href="https://fonts.googleapis.com/css?family=Montserrat:400,700" rel="stylesheet" type="text/css">
    <link href='https://fonts.googleapis.com/css?family=Kaushan+Script' rel='stylesheet' type='text/css'>
    <link href='https://fonts.googleapis.com/css?family=Droid+Serif:400,700,400italic,700italic' rel='stylesheet' type='text/css'>
    <link href='https://fonts.googleapis.com/css?family=Roboto+Slab:400,100,300,700' rel='stylesheet' type='text/css'>
    
    <!-- Theme CSS -->
    <link href="../css/agency.css" rel="stylesheet">
    <link href="../css/siczones.css" rel="stylesheet">

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
  print ('''<body>
     <!-- ==================== Nav Tabs ======================= -->
      <nav class="nav nav-tabs navbar-default navbar-fixed-top">
        <div class = "container">
        <ul class="nav nav-tabs">
          <li role="presentation"><a href="index.py"><span class="glyphicon glyphicon-home"/> Home</a></li>
          <li role="presentation"><a href="mode.py">Mode</a></li>
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
      <br/><br/><br>

      <div class="container-fluid">
        <div class="container">
        <div class="row">
          <div class="col-sm-3 col-md-3 col-xs-5">
            <!-- <img src="/img/brand.png" width="50px" height="50px" alt="Brand" style="display: block; margin-left: auto; margin-right: auto;"> -->
            <img src="/img/brand/Brand.png" style="max-height: 100px; display: block; margin-left: auto; margin-right: auto;" class="img-responsive" alt="Header">
            <br>
          </div>
          <div class="col-sm-9 col-md-9 col-xxs-7">
            <br>
            <brand style="display: block; margin-left: auto; margin-right: auto;">
                Safety in residential system
            </brand>
            <hr>
          </div>
        </div>
        </div>
      </div>
      <!-- ========================== Nav Tabs ======================= -->
          <div class = "container bg-all">
          <div class="wrapper">
          <center><fieldset>
          <h4 class="form-signin-heading">Status monitor !! Review Data from ThingSpeak</h4>
          <hr class="colorgraph">
          <div class="form-signin">''')
  i=1
  Field=[]
  device = ['RPi temp','Alert','Humidity','Voice','Light','Fire','Home Temp','Motion']
  while i<=8 :
          # Get data from fields 
          Field.append(form.getvalue('Field%s'%(i)))
          #print ('''<p class="form-control">Field%s : %s''' % (i,Field[i-1]))
          '''
          if Field[i-1] is not None:
                  uploadThingSpeak(Field[i-1],i)
                  if (form.getvalue('Field%s'%(i+1)) is not None):
                  #sleep for desired amount of time
                          time.sleep(sleep)
          '''
          print ('''
          <button href="#" data-toggle="modal"  data-target="#Field%s-modal" class="form-control" onmouseover="style.color='blue'" onmouseout="style.color='black'">%s <span class="label label-success pull-right">Field%s</span></button>
  					<div class="modal fade" id="Field%s-modal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true" style="display: none;">
  					<div class="modal-dialog" role="document">
  						<div class="modal-content">
                <div class="modal-header">
                  <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                  <h4 class="modal-title">%s</h4>
                </div>

                <div class="modal-body">
                  <div class="embed-responsive embed-responsive-16by9" style="overflow:auto;-webkit-overflow-scrolling:touch">
  							   <iframe class="embed-responsive-item" scrolling="auto" style="border: 1px solid #cccccc;" 
                   src="https://api.thingspeak.com/channels/125295/charts/%s?dynamic=true">
                   </iframe>
  						    </div>
                </div>

                <div class="modal-footer">
                  <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
                </div>
              </div>
  					</div>
  		  </div>'''% (i,device[i-1],i,i,device[i-1],i))
          i=i+1
  	
  print ('''</div><FORM><br><INPUT class="btn btn-lg btn-primary btn-block" Type="button" VALUE="Back" onClick="history.go(-1);return true;"></FORM>''')
  print ('''</fieldset></center></div></div>
  <!-- ============== Footer ============ -->
    <br/><br/><br/><div class="navbar navbar-default navbar-fixed-bottom">
      <div class="container">
        <p class="navbar-text pull-left">Copyright &copy; 2016 - Siczones.</p>
        <!-- a id="back-to-top" href="#" class="navbar-btn btn-danger btn pull-right" role="button" data-toggle="tooltip" data-placement="left"><span class="glyphicon glyphicon-chevron-up"></span></a -->

        <!-- Split button -->
        <div class="navbar-btn btn-group dropup pull-right">
          <button id="back-to-top" href="#" type="button" class="btn btn-warning"><span class="glyphicon glyphicon-chevron-up"></span> Top</button>
        </div>
      </div>  
  </div>
  <!-- ============== End Footer ============ -->
    </body></html>''')


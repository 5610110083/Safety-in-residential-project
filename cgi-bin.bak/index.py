#!/usr/bin/python 
#Import modules for CGI handling  
import cgi, cgitb
import Cookie, os, time 
import requests

# Instantiate a SimpleCookie object 
cookie = Cookie.SimpleCookie() 
cookie_string = os.environ.get('HTTP_COOKIE') 
# Create instance of FieldStorage  
form = cgi.FieldStorage()  
# Get data from fields
Username = form.getvalue('Username') 
Password = form.getvalue('Password')
status = 0

#check cookie login 
def loginCheker():
    if (Password == 'admin')&(Username == 'siczones'):
        return True
    else:
        return False

def setCookies(msg):
    global cookie
    s = requests.session()
    s.cookies.clear()
    cookie['login'] = msg
    #cookie['login']['secure'] = "secure"
    print cookie 

def getCookies():
    cookie_string = os.environ.get('HTTP_COOKIE') 
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
if loginCheker():
    setCookies('success') 
#print ("Location:192.168.0.102/") 
print ("Content-type:text/html\r\n\r\n") 
print ('''<!DOCTYPE html>
<html lang="en">
<head>
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

if (loginCheker()) or (getCookies()):
    # The SimpleCookie instance is a mapping 
    print ("<title>Welcome to server</title>") 
    print ('''<body>

     <!-- ==================== Nav Tabs ======================= -->
      <nav class="nav nav-tabs navbar-inverse navbar-fixed-top">
        <div class = "container">
        <ul class="nav nav-tabs">
          <li role="presentation" class="active"><a href="index.py">Home</a></li>
          <li role="presentation"><a href="mode.py">Mode</a></li>
          <li role="presentation" class="dropdown">
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
            <div class="wrapper">''')
    print ("<center><fieldset><legend>Hello !!</legend>")
    print ('''<h4 class="form-signin-heading" onmouseover="style.color='red'" onmouseout="style.color='black'" >Welcome to RPi server</h4>''')
    print ('<hr class="colorgraph"><br>')
    #print ("<h2>Hello %s %s</h2>" % (Username, Password)) 
    #print ('''<h4 class="form-signin-heading">Hello %s</h4>''' % (Username))
    print ('''<div class="form-signin">''')
    print ('''<form action="alert.py" class="btn-form"><button class="btn btn-lg btn-info btn-block" Type="submit" VALUE="Line" onmouseover="style.color='yellow'" onmouseout="style.color='white'">Alert</button></form>''')
    print ('''<form action="status.py" class="btn-form"><button class="btn btn-lg btn-info btn-block" Type="submit" VALUE="Status" onmouseover="style.color='yellow'" onmouseout="style.color='white'">Status</button></form>''')
    print ('''<form action="device.py" class="btn-form"><button class="btn btn-lg btn-info btn-block" Type="submit" VALUE="Status" onmouseover="style.color='yellow'" onmouseout="style.color='white'">Device</button></form>''')
    print ('''<form action="../UploadThingSpeak.html" class="btn-form"><button class="btn btn-lg btn-info btn-block" Type="submit" VALUE="Upload data to ThingSpeak" onmouseover="style.color='yellow'" onmouseout="style.color='white'">Cloud upload</button></form>''')
    print ('''<form action="mode.py" class="btn-form"><button class="btn btn-lg btn-info btn-block" Type="submit" VALUE="mode" onmouseover="style.color='yellow'" onmouseout="style.color='white'">Mode controls</button></form>''')
    print ('''<form action="#" class="btn-form"><button data-toggle="modal" data-target="#about-modal" class="btn btn-lg btn-primary btn-block" Type="contact" VALUE="line" onmouseover="style.color='yellow'" onmouseout="style.color='white'">About</button>
            <div class="modal fade" id="about-modal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true" style="display: none;">
            <div class="modal-dialog">
              <div class="loginmodal-container">
                <h2>RPi web server</h2>
                <p>
                    RPi web server design for support setting configuration mode,view status report,history log and systems testing.<br/>
                    <br/>Created by siczones.<br/>
                    Copyright (c) 2016.All rights reserved.<br/>
                    <button type="button" class="close" data-dismiss="modal">close[&times;]</button>
              </div>
            </div>
            </div></form>''')
    print ('''</div>''')
    print ('''<br><form action="logout.py" class="btn-form"><button class="btn btn-lg btn-danger btn-block" Type="submit" VALUE="logout" >Log out</button></form>''')
    print ("</fieldset></center></div></div>") 
else:
    print ("<title>Try Agian</title>")
    #url = HttpContext.Current.Request.Url.Host
    ip = '192.168.0.102'
    print ('''<meta http-equiv="refresh" content="5;http://%s">'''%(ip))
    print ("</head>") 
    print ('''<body><div class = "container">
                <div class="wrapper"><br/>''')
    print ("<center>")
    print ('''<fieldset><legend>Please try again!!</legend><hr class="colorgraph"><br>''')
    if "Username" or "Password":
        if "Username" not in form:
            print '''<h4 class="form-signin-heading">No username was entered</h4>'''
        if "Password" not in form:
            print '''<h4 class="form-signin-heading">No password was entered</h4>'''
    else:
        print '''<h4 class="form-signin-heading">Wrong account!</h4>'''
    print ("<p>This page will redirect in 5 sec.!</p>")
    print ('''<FORM ><INPUT class="btn btn-lg btn-primary btn-block" Type="button" VALUE="Back" onClick="history.go(-1);return true;" ></FORM>''')
    print ("</fieldset></center>")
    print ('''</div></div>''')
    
print ('''
  <!-- ============== Footer ============ -->
    <br/><br/><div class="navbar navbar-default navbar-fixed-bottom">
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

#!/usr/bin/python 
# -*- coding: utf-8 -*-f
#Import modules for CGI handling  
import cgi, cgitb
import Cookie, os, time 
import requests
from datetime import datetime
from uuid import getnode as get_mac
import fcntl, socket, struct

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
            
# Find client MAC_Addr        
def getHwAddr(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    info = fcntl.ioctl(s.fileno(), 0x8927,  struct.pack('256s', ifname[:15]))
    return ':'.join(['%02x' % ord(char) for char in info[18:24]])

# #===================== Start logCreate ======================#
def logCreate(login_status):
# When run as a cgi script, this will print the client's IP address.
	try:
		client_ip = cgi.escape(os.environ["REMOTE_ADDR"])
		#mac_addr = get_mac()
		mac_addr = getHwAddr('eth0')
	except:
		client_ip = 'Unknow'
		mac_addr = 'Unknow'

	with open("../logfiles/loginHistory.log", "a") as text_file:
		text_file.write("\r%s\t IP-Address: %s\t MAC-Address: %s\t\t Status: %s" %(time.ctime(), client_ip, mac_addr, login_status))
	return
#logCreate(login_status)
#===================== End logCreate ======================#

if loginCheker():
    setCookies('success')
    logCreate('success') 
else:
    logCreate('failed') 
	
#print ("Location:siczones.coe.psu.ac.th/") 
print ('''Content-type:text/html\r\n\r\n''') 
print ('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <link href="../favicon.ico" rel="icon" type="image/x-icon" />
    <link href="../favicon.ico" rel="shortcut icon" type="image/x-icon" />
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
        $(document).ready(function() {
            $(window).scroll(function() {
                if ($(this).scrollTop() > 50) {
                    $('#back-to-top').fadeIn();
                } else {
                    $('#back-to-top').fadeOut();
                }
            });
            // scroll body to 0px on click
            $('#back-to-top').click(function() {
                $('#back-to-top').tooltip('hide');
                $('body,html').animate({
                    scrollTop: 0
                }, 800);
                return false;
            });
            $('#back-to-top').tooltip('show');
        });
    </script>
	<style>
		.loader {
		  border: 16px solid #f3f3f3;
		  border-radius: 50%;
		  border-top: 16px solid #3498db;
		  width: 120px;
		  height: 120px;
		  -webkit-animation: spin 2s linear infinite;
		  animation: spin 2s linear infinite;
		}

		@-webkit-keyframes spin {
		  0% { -webkit-transform: rotate(0deg); }
		  100% { -webkit-transform: rotate(360deg); }
		}

		@keyframes spin {
		  0% { transform: rotate(0deg); }
		  100% { transform: rotate(360deg); }
		}
</style>
</head>''') 

if (loginCheker()) or (getCookies()):
	homeIP = 'siczones.coe.psu.ac.th/cgi-bin/index.py'
	print ('''<br><br><br><br><center><div class="loader"></div></center>''')
	print ('''<meta http-equiv="refresh" content="0.1;http://%s">'''%(homeIP))
else:
    print ('''<title>Try Agian</title>''')
    #url = HttpContext.Current.Request.Url.Host
    ip = 'siczones.coe.psu.ac.th'
    print ('''<meta http-equiv="refresh" content="5;http://%s">'''%(ip))
    print ('''</head>''') 
    print ('''<body><div class = "container">
                <div class="wrapper"><br>''')
    print ('''<center>''')
    print ('''<label>Please try again!!</label> <hr class="colorgraph"><br>''')
    
    if ("Username" not in form) and ("Password" not in form):
        print '''<h4 class="form-signin-heading">Wrong account!</h4>'''
    else:
        if "Username" not in form:
            print '''<h4 class="form-signin-heading">No username was entered</h4>'''
        if "Password" not in form:
            print '''<h4 class="form-signin-heading">No password was entered</h4>'''
		
    print ('''<p>This page will redirect in 5 sec.!</p>''')
    print ('''<FORM ><INPUT class="btn btn-lg btn-primary btn-block" Type="button" VALUE="Back" onClick="history.go(-1);return true;" ></FORM>''')
    print ('''</center>''')
    print ('''</div></div>''')
print ('''</html>''')

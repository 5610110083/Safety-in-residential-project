#!/usr/bin/python 
#Import modules for CGI handling  
import cgi, cgitb
import Cookie, os, time 
try:
  import pigpio 
except:
  pass
#============================ config ALERT ===================== #
import ConfigParser

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

#Reading config ALERT
def readALERT():
  try:
    ALERT = ConfigSectionMap('ALERT')
    return ALERT['status']
  except:
    print 'Data not found.'

# Update config ALERT
def writeALERT(value):
  # lets create that config file for next time...
  cfgfile = open("setting/config.ini",'wb')
  # add update the settings to the structure of the file, and lets write it out...
  Config.set('ALERT','status', value)
  Config.write(cfgfile)
  cfgfile.close()

#read ALERT from get method and config
cgitb.enable()
form=cgi.FieldStorage()
if "AlertStatus" not in form:
  #print 'data not input'
  status = readALERT()
  pass
else:
  status=form["AlertStatus"].value
  writeALERT(status)

#============================end config file ALERT ===================== #
# Reading test
# print readALERT()

# Writing test
# status = "ON"
# writeALERT(status)

'''
form = cgi.FieldStorage()  
AlertStatus = form.getvalue('AlertStatus')

if AlertStatus is None:
  AlertStatus = 'off'
'''
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
        
if getCookies() == False:
  print 'Content-Type: text/html\n' 
  print '<html><head>' 
  homeIP = '172.30.142.209'
  print ('''<meta http-equiv="refresh" content="0.1;http://%s">'''%(homeIP))
  print '</head></html>'
else:  
  print ("Content-type:text/html\r\n\r\n") 
  print ('''
<!DOCTYPE html>
<html lang="en">
<head>
<title>Alert</title>
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
    <link href="/css/agency.css" rel="stylesheet">
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
          <h4 class="form-signin-heading">Alert configuration</h4>
          
          <hr class="colorgraph"><br>
  		<!-- ////////////// Data //////////////// -->''')
  pin=4
  try:
    pi = pigpio.pi() # Connect to local Pi.
    pi.set_ALERT(pin, pigpio.OUTPUT)
    if AlertStatus == 'ON':
      pi.write(pin, 1) 
    elif AlertStatus == 'OFF':
      pi.write(pin, 0) 
    pi.stop() # Disconnect from local Pi.
  except:
    print """<label onmouseover="style.color='black'" onmouseout="style.color='red'">Are you sure your server that is running on RPi?</label>"""
    print "<p>Alert is not working!</p>"
    pass
  print('''
           <div class="form-signin">            
              <!-- ================= Enable | Disable ======================= -->
              <fieldset class="form-control btn-form"><label onmouseover="style.color='red'" onmouseout="style.color='black'">AlertStatus alert</label>
                  <form action="alert.py" method="GET" class="btn-group btn-group-justified" role="group" aria-label="...">
                        <div class="btn-group" role="group">
                          <button name="AlertStatus" VALUE="OFF" Type="submit" class="btn btn-default"><span class="label label-default ">OFF</span></button>
                        </div>
                        <div class="btn-group" role="group">
                          <button name="AlertStatus" VALUE="ON" Type="submit" class="btn btn-default"><span class="label label-danger">Alarm !!</span></button>
                        </div> 
                  </form>
              </fieldset>
              <br />
              <form action="lineAlert.py" class="btn-form"><button class="btn btn-lg btn-info btn-block" Type="submit" VALUE="Status" onmouseover="style.color='yellow'" onmouseout="style.color='white'">Line Alert</button></form>
              <form action="history.py" class="btn-form"><button class="btn btn-lg btn-info btn-block" Type="submit" VALUE="Status" onmouseover="style.color='yellow'" onmouseout="style.color='white'">History</button></form>
              ''')
  print('''
            </div>
      <!-- ////////////// End Data //////////////// -->
          <br><input class="btn btn-lg btn-primary btn-block" Type="button" VALUE="Back" onClick="history.go(-1);return true;">
          </fieldset></center>
          </div>
      </div>
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
  </body>''')

  print ("</html>")


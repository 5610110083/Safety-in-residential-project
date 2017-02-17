#!/usr/bin/python 
#Import modules for CGI handling  
import cgi, cgitb
from line import LineClient, LineGroup, LineContact
import Cookie, os, time
 
cookie = Cookie.SimpleCookie() 
cookie_string = os.environ.get('HTTP_COOKIE') 

form = cgi.FieldStorage()  
# Get data from fields
try:
  number = form.getvalue('number')
except:
  number = None
try:
  message = form.getvalue('message')
except:
  message = None
try:
  swStatus = form.getvalue('swStatus')
except:
  swStatus = None

if swStatus is None:
  swStatus = 'off'

client = ''
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

def loginLine():
	try:
		global client
		client = LineClient("sic@outlook.co.th", "1234567896")
		#client = LineClient(authToken="E1BfIh06jq9xX8j4ANU8.7s1VOrqGHwY0eQ+PV2DEwa.yPZkAqFnj3ROLP/caGZiCXgYyhCu+HBVf4NDfMy8/Bo=")
		#status = 'Login Success'
		return True
	except:
		#print "Login Failed"
		#status = "Login Failed"
		return False

def lineContacts():
    status = loginLine()
    if status is True :
            print ('''<p class="form-control">LINE login success,Please input form.</p>''')
	    #print loop friend
            print ('''<div height="250">''')
            for i in range(len(client.contacts)):
                      #print("No.{0} {name}".format(i, name = client.contacts[i]))
                      name = client.contacts[i]
                      name = str(name)
                      name = name.replace("<LineContact", "")
                      name = name.replace(">", "")
                      print('''<p class="form-label">No.%s : %s</p>''' %(i,name))
            print ('''</div>''')
            return True
    else :
            print ('''<p class="form-control">LINE login failed</p>''')
            return False

def lineGroups():
  status = loginLine()
  if status is True :
    print ('''<p class="form-control">LINE login success,Please input form.</p>''')
    #print loop friend
    print ('''<div height="250">''')
    for i in range(len(client.groups)):
      #print("No.{0} {name}".format(i, name = client.contacts[i]))
      name = client.groups[i]
      name = str(name)
      name = name.replace("<", "")
      name = name.replace("LineContact", "")
      name = name.replace("LineGroup", "")
      name = name.replace(">", "")
      print('''<p class="form-label">No.%s : %s</p>''' %(i,name))
    print ('''</div>''')
    return True
  else :
    print ('''<p class="form-control">LINE login failed</p>''')
    return False

def lineMessage(role,num,msg):
  msg = msg + '\n[Send by WebBot]'
  if role == 'contacts':
    friend = client.contacts[num]
  if role == 'groups':
    friend = client.groups[num]
  friend.sendMessage(msg)
  print('''<br/><p>Before send success</p>''')
  return

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
<title>LINE alert</title>
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
          <center><fieldset>
          <legend>LINE Alert</legend>
          <h4 class="form-signin-heading">Welcome to LINE Bot on page</h4>
          
          <hr class="colorgraph"><br>
          <!-- ////////////// Data //////////////// -->
          <div class="form-signin">

  <!-- ================= ON / OFF ======================= -->
          <form action="lineAlert.py" method="POST" class="btn-form"><button name="swStatus" class="btn btn-lg btn-default btn-block" Type="submit" ''')
  if swStatus == 'on':
    print('''VALUE="off" onmouseover="style.color='green'" onmouseout="style.color='black'">On | Off<span class="label label-success pull-right">Enable</span></button></form>''')
  elif swStatus == 'off':
    print('''VALUE="on" onmouseover="style.color='red'" onmouseout="style.color='black'">On | Off<span class="label label-danger pull-right">Disable</span></button></form>''')

  #============= SEND MESSEGE FRIENDS =================#
  print('''<form action="#" class="btn-form"><button data-toggle="modal" data-target="#line-modal-client" class="btn btn-lg btn-info btn-block" Type="contact" VALUE="line" onmouseover="style.color='yellow'" onmouseout="style.color='white'">Friends</button>
  			      <div class="modal fade" id="line-modal-client" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true" style="display: none;">
  			      <div class="modal-dialog">
  				    <div class="loginmodal-container">''')
  result = lineContacts()
  if result is True:
  	print('''	<br/><form action="lineAlert.py" method="post">
  						<input type="number" class="form-control" name="number" placeholder="Contact No." required="" autofocus="" min="0" max="%s" />'''%(len(client.contacts)-1))
  	print('''	<input type="text" class="form-control" name="message" placeholder="message" required=""/>   
  						<br/>
  						<button class="btn btn-lg btn-success btn-block" value="Send" type="Submit" onmouseover="style.color='yellow'" onmouseout="style.color='white'">Send</button> 
  						<button class="btn btn-lg btn-danger btn-block" value="Reset" type="Reset" onmouseover="style.color='red'" onmouseout="style.color='white'">Reset</button> 			
  					</form>''')
  	if number is not None:
  		number = int(number)
  		lineMessage('contacts',number,message)
  else:
  	print('''<h4>Please reload webpage in nexttime.</h4><br>''')
  print(''' </br><button type="button" class="close" data-dismiss="modal">close[&times;]</button>
                </div>
  			        </div>
  			        </div>
  		      </form>''')

    #============= SEND MESSEGE GROUP =================#
  print('''<form action="#" class="btn-form"><button data-toggle="modal" data-target="#line-modal-group" class="btn btn-lg btn-info btn-block" Type="contact" VALUE="line" onmouseover="style.color='yellow'" onmouseout="style.color='white'">Groups</button>
              <div class="modal fade" id="line-modal-group" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true" style="display: none;">
              <div class="modal-dialog">
              <div class="loginmodal-container">''')
  result = lineGroups()
  if result is True:
    print(''' <br/><form action="lineAlert.py" method="post">
              <input type="number" class="form-control" name="number" placeholder="Group No." required="" autofocus="" min="0" max="%s" />'''%(len(client.groups)-1))
    print(''' <input type="text" class="form-control" name="message" placeholder="message" required=""/>   
              <br/>
              <button class="btn btn-lg btn-success btn-block" value="Send" type="Submit" onmouseover="style.color='yellow'" onmouseout="style.color='white'">Send</button> 
              <button class="btn btn-lg btn-danger btn-block" value="Reset" type="Reset" onmouseover="style.color='red'" onmouseout="style.color='white'">Reset</button>       
            </form>''')
    if number is not None:
      number = int(number)
      lineMessage('groups',number,message)
  else:
    print('''<h4>Please reload webpage in nexttime.</h4><br>''')
  print(''' </br><button type="button" class="close" data-dismiss="modal">close[&times;]</button>
                </div>
                </div>
                </div>
            </form>''')

  print(''' </div><br/>
            <form action="alert.py"><button class="btn btn-lg btn-primary btn-block" VALUE="Back">Back</button></form>
          </fieldset></center>
          </div>
      </div>
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

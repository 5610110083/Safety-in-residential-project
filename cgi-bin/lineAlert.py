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

client = ''
NetConnectionStatus = False
def loginLine():
	try:
		global client
		client = LineClient("sic@outlook.co.th", "1234567896")
		#client = LineClient(authToken="E1BfIh06jq9xX8j4ANU8.7s1VOrqGHwY0eQ+PV2DEwa.yPZkAqFnj3ROLP/caGZiCXgYyhCu+HBVf4NDfMy8/Bo=")
		#status = 'Login Success'
    # NetConnectionStatus = True
		return True
	except:
    # global NetConnectionStatus
		#print "Login Failed"
		#status = "Login Failed"
		return False

def lineContacts():
    status = loginLine()
    if status is True :
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
            print ('''<p class="form-control">LINE login failed!</p>''')
            return False

def lineGroups():
  status = loginLine()
  if status is True :
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
    print ('''<p class="form-control">LINE login failed!</p>''')
    return False

def lineMessage(role,num,msg):
  msg = msg + '\n[Send by WebBot]'
  if role == 'contacts':
    friend = client.contacts[num]
  if role == 'groups':
    friend = client.groups[num]
  friend.sendMessage(msg)
  print('''<br/><b>Before send success!</b>''')
  return

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
<title>LINE alert</title>
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
</head>''') 
  print ('''
  <body>
      <div class = "container bg-all">        
          <div class="wrapper">
          <center><fieldset>
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
  #============= Test LINE Alert =================#
  print ("""<form action="notify.py" target="_blank" class="btn-form"><button class="btn btn-lg btn-info btn-block" Type="submit" name="data" VALUE="Test" onmouseover="style.color='yellow'" onmouseout="style.color='white'">Test LINE Alert</button></form>""")
  
  #============= SEND MESSEGE FRIENDS =================#
  print('''<form action="#" class="btn-form"><button data-toggle="modal" data-target="#line-modal-client" class="btn btn-lg btn-info btn-block disabled" Type="contact" VALUE="line" onmouseover="style.color='yellow'" onmouseout="style.color='white'">Friends</button>
  			      <div class="modal fade" id="line-modal-client" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true" style="display: none;">
  			      <div class="modal-dialog">
  				    <div class="loginmodal-container">

              <form action="lineAlert.py" method="post">
                <div class="modal-header">
                  <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                  <h4 class="modal-title" id="exampleModalLabel">LINE Client message</h4>
                </div>
                <div class="modal-body">
              ''')
  result = lineContacts()
  if result is True:
  	print('''	<br/>
  						<input type="number" class="form-control" name="number" placeholder="Contact No." required="" autofocus="" min="0" max="%s" />'''%(len(client.contacts)-1))
  	print('''	<input type="text" class="form-control" name="message" placeholder="Message" required=""/> ''')
  	if number is not None:
  		number = int(number)
  		lineMessage('contacts',number,message)
  else:
  	print('''<h4>Please reload webpage in nexttime.</h4><br>''')
  print(''' 
                  </div>
                  <div class="modal-footer">
                    <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
                    <button type="Reset" class="btn btn-danger" value="Reset" onmouseover="style.color='red'" onmouseout="style.color='white'">Reset</button> 
                    <button type="Submit" class="btn btn-success" value="Send" onmouseover="style.color='yellow'" onmouseout="style.color='white'">Send message</button>
                  </div>
                </form>
                
                </div>
  			        </div>
  			        </div>
  		      </form>''')

    #============= SEND MESSEGE GROUP =================#
  print('''<form action="#" class="btn-form">
              <button data-toggle="modal" data-target="#line-modal-group" class="btn btn-lg btn-info btn-block" Type="contact" VALUE="line" onmouseover="style.color='yellow'" onmouseout="style.color='white'">Groups</button>
              <div class="modal fade" id="line-modal-group" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true" >
              <div class="modal-dialog">
              <div class="loginmodal-container">

              <form action="lineAlert.py" method="post">
                <div class="modal-header">
                  <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                  <h4 class="modal-title" id="exampleModalLabel">LINE Group message</h4>
                </div>
                <div class="modal-body">
          ''')
  result = lineGroups()
  if result is True:
    print(''' <br/>
              <input type="number" class="form-control" name="number" placeholder="Group No." required="" autofocus="" min="0" max="%s" />'''%(len(client.groups)-1))
    print(''' <input type="text" class="form-control" name="message" placeholder="Message" required=""/>''')
    if number is not None:
      number = int(number)
      lineMessage('groups',number,message)
  else:
    print('''<h4>Please reload webpage in nexttime.</h4>''')
  print('''
                  </div>
                  <div class="modal-footer">
                    <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
                    <button type="Reset" class="btn btn-danger" value="Reset" onmouseover="style.color='yellow'" onmouseout="style.color='white'">Reset</button> 
                    <button type="Submit" class="btn btn-success" value="Send" onmouseover="style.color='yellow'" onmouseout="style.color='white'">Send message</button>
                  </div>
                </form>

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

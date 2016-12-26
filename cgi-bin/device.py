#!/usr/bin/python 
#Import modules for CGI handling  
import cgi, cgitb
import Cookie, os, time 

form = cgi.FieldStorage()  
device1 = form.getvalue('device1')
if device1 is None:
	device1 = 'on'
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
	print ('''<!DOCTYPE html>
  <html lang="en">
<head>
<title>Device</title>
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
          <h4 class="form-signin-heading">Check device as active or not</h4>
          
          <hr class="colorgraph"><br>
  		<!-- ////////////// Data //////////////// -->
  		<div class="form-signin">
      		<!-- ================= Enable | Disable ======================= -->
  			<form action="device.py" method="POST" class="btn-form"><button name="device1" class="btn btn-lg btn-default btn-block" Type="submit" ''')
	if device1 == 'on':
		print('''VALUE="off" onmouseover="style.color='green'" onmouseout="style.color='black'">On | Off<span class="label label-success pull-right">Enable</span></button></form>''')
	elif device1 == 'off':
		print('''VALUE="on" onmouseover="style.color='red'" onmouseout="style.color='black'">On | Off<span class="label label-danger pull-right">Disable</span></button></form>''')
	print('''
		</div>
      <!-- ////////////// End Data //////////////// -->
          <br><form action="index.py"><button class="btn btn-lg btn-primary btn-block" VALUE="Back">Back</button></form>
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
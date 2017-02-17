#!/usr/bin/python 
# -*- coding: utf-8 -*-f
#Import modules for CGI handling  
import cgi, cgitb
import Cookie, os, time 

form = cgi.FieldStorage()  
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
	homeIP = 'siczones.coe.psu.ac.th'
	print ('''<meta http-equiv="refresh" content="0.1;http://%s">'''%(homeIP))
	print '</head></html>'
else:
	print ("Content-type:text/html\r\n\r\n") 
	print ('''
	<!DOCTYPE html>
	<html lang="en">
	<head>
	<meta charset="utf-8">
	<title>Welcome to server</title>
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
		<div class="container">
			<ul class="nav nav-tabs">
				<li role="presentation" class="active">
					<a href="index.py"><span class="glyphicon glyphicon-home" /> Home</a>
				</li>
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
	<br>
	<br>
	<br>
	<div class="container-fluid">
		<div class="container">
			<div class="row">
				<div class="col-sm-4 col-md-3 col-xs-5">
					<!-- <img src="/img/brand.png" width="50px" height="50px" alt="Brand" style="display: block; margin-left: auto; margin-right: auto;"> -->
					<img src="/img/brand/Brand.png" style="max-height: 100px; display: block; margin-left: auto; margin-right: auto;" class="img-responsive" alt="Header">
					<br>
				</div>
				<div class="col-sm-8 col-md-9 col-xxs-7">
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
	<div class="container bg-all">
		<div class="wrapper">
			<center>
				<h3 class="form-signin-heading" onmouseover="style.color='red'" onmouseout="style.color='black'">Welcome to RPi server</h3>
				<hr class="colorgraph">
				<br>
				<div class="form-signin">
					<form action="Quick_Start.py" class="btn-form">
						<button class="disabled btn btn-lg btn-info btn-block" Type="submit" VALUE="Line" onmouseover="style.color='yellow'" onmouseout="style.color='white'">Quick Start Guide!</button>
					</form>
					<form action="alert.py" class="btn-form">
						<button class="btn btn-lg btn-info btn-block" Type="submit" VALUE="Line" onmouseover="style.color='yellow'" onmouseout="style.color='white'">Alert</button>
					</form>
					<form action="status.py" class="btn-form">
						<button class="btn btn-lg btn-info btn-block" Type="submit" VALUE="Status" onmouseover="style.color='yellow'" onmouseout="style.color='white'">Status</button>
					</form>
					<form action="device.py" class="btn-form">
						<button class="btn btn-lg btn-info btn-block" Type="submit" VALUE="Status" onmouseover="style.color='yellow'" onmouseout="style.color='white'">Device</button>
					</form>
					<form action="../UploadThingSpeak.html" class="btn-form">
						<button class="btn btn-lg btn-info btn-block" Type="submit" VALUE="Upload data to ThingSpeak" onmouseover="style.color='yellow'" onmouseout="style.color='white'">Test cloud upload</button>
					</form>
					<form action="mode.py" class="btn-form">
						<button class="btn btn-lg btn-info btn-block" Type="submit" VALUE="mode" onmouseover="style.color='yellow'" onmouseout="style.color='white'">Mode controls</button>
					</form>
					<form action="loginHistory.py" class="btn-form">
						<button class="btn btn-lg btn-info btn-block" Type="submit" VALUE="mode" onmouseover="style.color='yellow'" onmouseout="style.color='white'">Login history</button>
					</form>
					<hr>
					<div  class="btn-form">
					<button data-toggle="modal" data-target="#reset-setting" class="btn btn-lg btn-danger btn-block " onmouseover="style.color='yellow'" onmouseout="style.color='white'">Reset all setting</button> 
					</div>
					<div class="modal fade" id="reset-setting" tabindex="-1" role="dialog" aria-labelledby="Reset all setting to default" aria-hidden="true" style="display: none;">
						<form action="reset.py" target="_blank" method="post" class="modal-dialog">
						<div class="loginmodal-container">
						      <div class="modal-header">
						            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
						            <h4 class="modal-title" id="exampleModalLabel">Are you sure?</h4>
						      </div>
						      <div class="modal-body">
						            <p>After you click reset , the system will reset all setting to default.</p>						            
						       </div>
						       <div class="modal-footer">
						           <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
						           <button type="submit" class="disabled btn btn-danger" value="submit">Reset</button>
						       </div>
						</div>
						</form>
					</div>

					<div  class="btn-form">
					<button data-toggle="modal" data-target="#about-modal" class="btn btn-lg btn-success btn-block" Type="contact" VALUE="line" onmouseover="style.color='yellow'" onmouseout="style.color='white'">About</button>
					</div>
					<div class="modal fade" id="about-modal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true" style="display: none;">
						<div class="modal-dialog" role="document">
							<div class="modal-content">
								<div class="modal-header">
									<button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
									<h4 class="modal-title">RPi web server About</h4>
								</div>
								<div class="modal-body">
									<div class="container-fluid">
										<p>
											RPi Web Server design for supports setting: Configuration Mode, View Status Report, History Logs, Systems Testing, and so on.
											<br>
											<br>
											<a href="https://line.me/R/ti/p/%40kkx7460v" target="_blank"><img height="30" border="1" alt="add_friends" src="https://scdn.line-apps.com/n/line_add_friends/btn/en.png"></a>
											<br>
											<br>Created by siczones.
											<br> Copyright &copy; 2016-2017. All rights reserved.
										</p>
									</div>
								</div>
								<div class="modal-footer">
									<button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
								</div>
							</div>
						</div>
					</div>
				</div>
				<br>
				<form action="newAccount.py" class="btn-form">
					<button class="disabled btn btn-lg btn-warning btn-block" Type="submit" VALUE="newAcc" onmouseover="style.color='yellow'" onmouseout="style.color='white'">Create new account!</button>
				</form>
				<form action="logout.py" class="btn-form">
					<button class="btn btn-lg btn-danger btn-block" Type="submit" VALUE="logout">Log out</button>
				</form>
			</center>
		</div>
	</div>
    ''')
	print ('''
	<!-- ============== Footer ============ -->
	<br/>
	<br/>
	<br/>
	<div class="navbar navbar-default navbar-fixed-bottom">
		<div class="container">
			<p class="navbar-text pull-left">Copyright &copy; 2016-2017 Siczones.</p>
			<!-- a id="back-to-top" href="#" class="navbar-btn btn-danger btn pull-right" role="button" data-toggle="tooltip" data-placement="left"><span class="glyphicon glyphicon-chevron-up"></span></a -->

			<!-- Split button -->
			<div class="navbar-btn btn-group dropup pull-right">
				<button id="back-to-top" href="#" type="button" class="btn btn-warning"><span class="glyphicon glyphicon-chevron-up"></span> Top</button>
			</div>
		</div>
	</div>
	<!-- ============== End Footer ============ -->
	</body>
	</html>
	''')

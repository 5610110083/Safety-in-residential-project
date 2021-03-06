#!/usr/bin/python
# -*- coding: utf-8 -*-

# Import modules for CGI handling

import cgi
import cgitb
import Cookie
import os
import time

# =====================***** C-o-n-f-i-g--m-o-d-e *****================ #

import ConfigParser

Config = ConfigParser.ConfigParser()
Config.read(r'setting/devices.ini')
settingSec = Config.sections()


# print settingSec

def ConfigSectionMap(device_No):
    dict1 = {}
    options = Config.options(device_No)
    for option in options:
        try:
            dict1[option] = Config.get(device_No, option)
            if dict1[option] == -1:
                DebugPrint('skip: %s' % option)
        except:
            print 'exception on %s!' % option
            dict1[option] = None
    return dict1


# ==============Reading config of device=============

def getAmount():
    try:
        amountDevice = ConfigSectionMap('NumDevice')
        return amountDevice['amount']
    except:
        print 'Data not found.'
        return 0


def getName(device_No):
    try:
        Device = ConfigSectionMap('Device' + str(device_No))
        return Device['name']
    except:
        return 'Data not found.'


def getAPI_key(device_No):
    try:
        Device = ConfigSectionMap('Device' + str(device_No))
        return Device['api-key']
    except:
        return 'Data not found.'


def getMaxMin(device_No):
    try:
        Device = ConfigSectionMap('Device' + str(device_No))
        return Device['alert_type']
    except:
        return 'Data not found.'


def getThreadHole(device_No):
    try:
        Device = ConfigSectionMap('Device' + str(device_No))
        return Device['decision_point']
    except:
        return 'Data not found.'


# ============== End Reading config of device =============

# ============== Update config MODE =======================

def amount(value):
    cfgfile = open(r'setting/devices.ini', 'wb')
    Config.set('NumDevice', 'amount', value)
    Config.write(cfgfile)
    cfgfile.close()


def setName(device_No, value):

    # Uncomment add if you create new section or uncomment read when you want to update
    # config.add_section('Device1')
    # config.read(r'setting/devices.ini')
    # lets create that config file for next time...

    cfgfile = open(r'setting/devices.ini', 'wb')
    Config.set('Device' + str(device_No), 'name', value)
    Config.write(cfgfile)
    cfgfile.close()


#setName(1, 'Temp & Humid.')  # test


def setAPI_key(device_No, value):
    cfgfile = open(r'setting/devices.ini', 'wb')
    Config.set('Device' + str(device_No), 'api-key', value)
    Config.write(cfgfile)
    cfgfile.close()


def setMaxMin(device_No, value):
    cfgfile = open(r'setting/devices.ini', 'wb')
    Config.set('Device' + str(device_No), 'alert_type', value)
    Config.write(cfgfile)
    cfgfile.close()


def setThreadHole(device_No, value):
    cfgfile = open(r'setting/devices.ini', 'wb')
    Config.set('Device' + str(device_No), 'decision_point', value)
    Config.write(cfgfile)
    cfgfile.close()


# ============== End Update config MODE =======================

# =====================***** E-n-d  C-o-n-f-i-g--m-o-d-e *****================ #

#when edit device
form = cgi.FieldStorage()
DeviceName1  = form.getvalue('Device-name1')
DeviceName2  = form.getvalue('Device-name2')
DeviceName3  = form.getvalue('Device-name3')
DeviceName4  = form.getvalue('Device-name4')
AlertTh = form.getvalue('Alert-th')
maxMin = form.getvalue('max-min')
Device_No = 0

if DeviceName1 is not None:
	Device_No = 1
	setName(Device_No, DeviceName1)
	setMaxMin(Device_No, maxMin)
	setThreadHole(Device_No, AlertTh)
elif DeviceName2 is not None:
	Device_No = 2
	setName(Device_No, DeviceName2)
	setMaxMin(Device_No, maxMin)
	setThreadHole(Device_No, AlertTh)
elif DeviceName3 is not None:
	Device_No = 3
	setName(Device_No, DeviceName3)
	setMaxMin(Device_No, maxMin)
	setThreadHole(Device_No, AlertTh)
elif DeviceName4 is not None:
	Device_No = 4
	setName(Device_No, DeviceName4)
	setMaxMin(Device_No, maxMin)
	setThreadHole(Device_No, AlertTh)
else:
	pass


#when add device
newDeviceName = form.getvalue('Device-name-add') 
newapiKeyDevice = form.getvalue('api-key-device-add')

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
	  <center>
	  <h4 class="form-signin-heading">Device configurations</h4>
	  
	  <hr class="colorgraph"><br>
	
	
	<!-- ======================== Data ======================== -->
	<div class="form-signin">
	''')
	
	print ('''<hr><label>Change of option: </label><br>
	DeviceName1  = %s <br>
	DeviceName2  = %s <br>
	DeviceName3  = %s <br>
	DeviceName4  = %s <br>
	AlertTh = %s <br>
	maxMin = %s <br>
	<hr>'''%(DeviceName1,DeviceName2,DeviceName3,DeviceName4,AlertTh,maxMin))
	num_device = int(float(getAmount()))
	i = 0
	while i < num_device:
		i = i + 1
		print ('''<!-- ======================== Device%s ======================== -->''') %(str(i))
		print ('''
		
		<div class="panel panel-info">
		<button class="panel-heading btn btn-sm btn-block" data-toggle="collapse" data-target="#Device%s" aria-expanded="false" aria-controls="collapseFull-Active" type="button"">
			<label class="panel-title">Device%s : %s</label>
		</button>
		<div class="collapse" id="Device%s">
			<div class="panel-body">
				<div class="row">
					<div class="col-sm-6">
						<button type="button" class="btn btn-block btn-sm btn-default" data-toggle="modal" data-target="#edit-device-%s">Edit</button>
					</div>
					<div class="col-sm-6">
						<button type="button" class="disabled btn btn-block btn-sm btn-danger" data-toggle="modal" data-target="#remove-device">Remove</button>
					</div>
				</div>				
			
			
			</div>
		</div>
		</div>
		<br>
		''')%(str(i), str(i), getName(i), str(i), str(i))
		print ('''<!-#============= Edit device %s =================# -->''')%(str(i))
		print ('''
		<div class="modal fade" id="edit-device-%s" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true" style="display: none;">
			<form action="#" method="get" class="modal-dialog">
				<div class="loginmodal-container">
					<div class="modal-header">
						<button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
						<h4 class="modal-title" id="">Edit device setting</h4>
					</div>
					<div class="modal-body">
						<div class="row">
							<div class="col-lg-12">
								<input type="text" class="form-control" name="Device-name%s" placeholder="%s" required="">																
							</div>
							<div class="col-lg-12">
								<div class="input-group">
									<input type="number" step="0.01" class="form-control" name="Alert-th" placeholder="Thread-Hole (Current:%s)" required="" />
									<span class="input-group-addon">									
										<input type="radio" name="max-min" value="max" aria-label="Max" checked>Max
									</span>
									<span class="input-group-addon">
										<input type="radio" name="max-min" value="min" aria-label="Min">Min									
									</span>
								</div>
								<!-- /input-group -->
							</div>							
						</div>
						<!-- /.row -->
						<div class="alert alert-warning alert-dismissable fade in" role="alert">
							<p>Max : Alert  when sensor value maximum than threadhold.</p>
							<p>Min : Alert  when sensor value minimum than threadhold.</p>
						</div>
					</div>
					<div class="modal-footer">
						<button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
						<button type="Reset" class="btn btn-danger" value="Reset" onmouseover="style.color='red'" onmouseout="style.color='white'">Reset</button>
						<button type="submit" class="btn btn-success" value="submit" onmouseover="style.color='yellow'" onmouseout="style.color='white'">Update</button>
					</div>
				</div>
			</form>
		</div>
		''')%(str(i), str(i), getName(i), getThreadHole(i))
	print('''
      
  		<!-#============= Add device =================# -->
		
		<button data-toggle="modal" data-target="#add-device" class="btn btn-block btn-success btn-lg" onmouseover="style.color='yellow'" onmouseout="style.color='white'"><span class="glyphicon glyphicon-plus"> ADD</span></button>
		
		<div class="modal fade" id="add-device" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true" style="display: none;">
			<form action="#" method="get" class="modal-dialog">
				<div class="loginmodal-container">
					<div class="modal-header">
						<button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
						<h4 class="modal-title" id="exampleModalLabel">Add device</h4>
					</div>
					<div class="modal-body">
						<div class="row">
							<div class="col-lg-12">
								<input type="text" class="form-control" name="Device-name-add" placeholder="Name" required="">
								<input type="text" class="form-control" name="api-key-device-add" placeholder="API-Key" required="">
							</div>
							<div class="col-lg-12">
								<div class="input-group">
									<input type="number" step="0.01" class="form-control" name="Alert-th" placeholder="Thread-Hole" required="" />
									<span class="input-group-addon">									
										<input type="radio" name="max-min" aria-label="Max" checked>Max
									</span>
									<span class="input-group-addon">
										<input type="radio" name="max-min" aria-label="Min">Min									
									</span>
								</div>
								<!-- /input-group -->
							</div>
						</div>
						<!-- /.row -->
					</div>
					<div class="modal-footer">
						<button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
						<button type="Reset" class="btn btn-danger" value="Reset" onmouseover="style.color='red'" onmouseout="style.color='white'">Reset</button>
						<button type="submit" class="btn btn-success" value="submit" onmouseover="style.color='yellow'" onmouseout="style.color='white'">OK</button>
					</div>
				</div>
			</form>
		</div>
      <!-- ======================== End Data ======================== -->
		</center>
		</div>
		<form action="index.py"><button class="btn btn-lg btn-primary btn-block" VALUE="Back">Back</button></form>
		<br><br>
      </div>
  <!-- ============== Footer ============ -->
		<br><br><div class="navbar navbar-default navbar-fixed-bottom">
      <div class="container">
        <p class="navbar-text pull-left">Copyright © 2016-2017 Siczones.</p>
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

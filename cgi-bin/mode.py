#!/usr/bin/python 
#Import modules for CGI handling  
import cgi, cgitb
import Cookie, os, time 
#============================ config mode ===================== #
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

#Reading config mode
def readMode():
  try:
    MODE = ConfigSectionMap('MODE')
    return MODE['mode']
  except:
    print 'Data not found.'
    return 0

# Update config MODE
def writeMode(value):
  # lets create that config file for next time...
  cfgfile = open("setting/config.ini",'wb')
  # add update the settings to the structure of the file, and lets write it out...
  Config.set('MODE','mode', value)
  Config.write(cfgfile)
  cfgfile.close()

#read mode from get method and config
cgitb.enable()
form=cgi.FieldStorage()
if "currentMode" not in form:
  #print 'data not input'
  numMode = readMode()
  pass
else:
  modeVal=form["currentMode"].value
  writeMode(modeVal)
  numMode = modeVal

#============================end config file mode ===================== #

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
      <meta charset="utf-8">
      <!-- This file has been downloaded from Bootsnipp.com. Enjoy! -->
      <title>Mode</title>
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <link href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.0/css/bootstrap.min.css" rel="stylesheet">
      <link href="../favicon.ico" rel="icon" type="image/x-icon"/>     
      <link href="../favicon.ico" rel="shortcut icon" type="image/x-icon"/>
      
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
          //scroll body to 0px on click
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

    <!-- Custom Fonts -->
    <link href="/vendor/font-awesome/css/font-awesome.min.css" rel="stylesheet" type="text/css">
    <link href="https://fonts.googleapis.com/css?family=Montserrat:400,700" rel="stylesheet" type="text/css">
    <link href='https://fonts.googleapis.com/css?family=Kaushan+Script' rel='stylesheet' type='text/css'>
    <link href='https://fonts.googleapis.com/css?family=Droid+Serif:400,700,400italic,700italic' rel='stylesheet' type='text/css'>
    <link href='https://fonts.googleapis.com/css?family=Roboto+Slab:400,100,300,700' rel='stylesheet' type='text/css'>
    
    <!-- Theme CSS -->
    <link href="../css/agency.css" rel="stylesheet">
    <link href="../css/siczones.css" rel="stylesheet">
  </head>''') 
  print ('''
  <body>
      <!-- ==================== Nav Tabs ======================= -->
      <nav class="nav nav-tabs navbar-default navbar-fixed-top">
        <div class = "container">
        <ul class="nav nav-tabs">
          <li role="presentation"><a href="index.py"><span class="glyphicon glyphicon-home"/> Home</a></li>
          <li role="presentation" class="active"><a href="mode.py">Mode</a></li>
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
          <h4 class="form-signin-heading">Configuration mode</h4>
          <hr class="colorgraph"><br>''')
  print('''
      <!-- ========================== Data ========================= -->
      <div class="form-signin">

                                                          <!-- ============Off button ==============-->
          <form action="mode.py" class="btn-form" method="get">
          <button data-toggle="modal"  data-target="#login-modal-off" class="btn btn-lg btn-danger btn-block" name="currentMode" value="1" type="submit"  onmouseover="style.color='pink'" onmouseout="style.color='white'">
          OFF
      ''')
  # Off mode
  if numMode is '1':
    print('''<span class="label label-success glyphicon glyphicon-ok pull-right"> </span>''')

  print('''
          </button>
          <div class="modal fade" id="login-modal-off" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true" style="display: none;">
              <div class="modal-dialog">
                <div class="loginmodal-container">
                  <h4>OFF Success</h4><br>
                  </br><button type="button" class="close" data-dismiss="modal">close[&times;]</button>        
                </div>
              </div>
          </div>
      </form>

                                                          <!-- ============Basic button ==============-->
      <form action="mode.py" class="btn-form" method="get">
          <button data-toggle="modal"  data-target="#login-modal-basic" class="btn btn-lg btn-warning btn-block" name="currentMode" value="2" type="submit" onmouseover="style.color='pink'" onmouseout="style.color='white'">
      BASIC 
      ''')
  # Basic mode
  if numMode is '2':
    print('''<span class="label label-success glyphicon glyphicon-ok pull-right"> </span>''')

  print('''
      </button>
        <div class="modal fade" id="login-modal-basic" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true" style="display: none;">
        <div class="modal-dialog">
          <div class="loginmodal-container">
            <h4>Basic mode active</h4><br>
            </br><button type="button" class="close" data-dismiss="modal">close[&times;]</button>         
          </div>
        </div>
        </div>
      </form>

                                                        <!-- ============Full button ==============-->
      <form action="mode.py" class="btn-form" method="get">
        <button data-toggle="modal"  data-target="#login-modal-full" class="btn btn-lg btn-success btn-block" name="currentMode" value="3" type="submit" onmouseover="style.color='#33FF33'" onmouseout="style.color='white'">
        FULL 
      ''')
  # Full mode
  if numMode is '3':
    print('''<span class="label label-success glyphicon glyphicon-ok pull-right"> </span>''')

  print('''
        </button>
        <div class="modal fade" id="login-modal-full" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true" style="display: none;">
        <div class="modal-dialog">
          <div class="loginmodal-container">
            <h4>Full mode active</h4><br> 
            </br><button type="button" class="close" data-dismiss="modal">close[&times;]</button>       
          </div>
        </div>
        </div>    
      </form>
  ''')
  print('''

                                            <!-- ============Advance button ==============-->
      <div class="panel panel-info">
                <button class="panel-heading btn btn-lg btn-info btn-block" type="button" data-toggle="collapse" data-target="#collapseAdvance" aria-expanded="false" aria-controls="collapseAdvance">
                  <h3 class="panel-title">
                  Advance
  ''')
  # Advance mode
  if numMode is '4':
    print('''       <span class="label label-success glyphicon glyphicon-ok pull-right"> </span> ''')
  print('''    
                  </h3>
                </button>
                <div class="collapse" id="collapseAdvance">
                  <div class="panel-body">
                  <form action="mode.py" class="btn-form" method="get">
                    <table class="table table-striped">
                      <thead>
                        <tr>
                          <th><span>Sensor type</span></th>
                          <th><span>Check for enable</span></th>
                        </tr>
                      </thead>
                      <tbody>
                        <!-- first sensor -->
                        <tr>
                          <td>
                            Temp Sensor
                          </td>
                          <td>
                            <input type="checkbox" aria-label="Temp.">
                          </td>
                        </tr>
                        <!-- second sensor -->
                        <tr>
                          <td>
                            Voice detect Sensor
                          </td>
                          <td>
                            <input type="checkbox" aria-label="Temp.">
                          </td>
                        </tr> 
                        <!-- third sensor -->
                        <tr>
                          <td>
                            Fire & Smoke Sensor
                          </td>
                          <td>
                            <input type="checkbox" aria-label="Temp.">
                          </td>
                        </tr>
						<!-- fourth sensor -->
                        <tr>
                          <td>
                            PIR Motion Sensor
                          </td>
                          <td>
                            <input type="checkbox" aria-label="Temp.">
                          </td>
                        </tr>							
                      </tbody>
                    </table>

                        <!-- apply button -->
                        <button data-toggle="modal"  data-target="#login-modal-advance" class="btn btn-success" name="currentMode" value="4" type="submit" onmouseover="style.color='#33FF33'" onmouseout="style.color='white'">
                        Apply
                        </button>

                            <!--show in advance modal -->
                            <div class="modal fade" id="login-modal-advance" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true" style="display: none;">
                            <div class="modal-dialog">
                              <div class="loginmodal-container">
                                <h4>Advance active</h4><br>
                                </br><button type="button" class="close" data-dismiss="modal">close[&times;]</button>         
                              </div>
                            </div>
                            </div>

                        <!-- reset button -->
                        <button class="btn btn-primary" name="Reset" value="Reset" type="Reset" onmouseover="style.color='red'" onmouseout="style.color='white'">
                            Reset
                        </button>

                    </form>
                  </div>
                </div>
        </div>
       
  ''')     
  print(''' 
      </div>
      <br>

      <!-- back button -->
      <form action="index.py"><button class="btn btn-lg btn-primary btn-block" VALUE="Back">Back</button></form>

      </fieldset></center>
      </div>
      </div>


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
  </body>''')

  print ("</html>")
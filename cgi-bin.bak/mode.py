#!/usr/bin/python 
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
        <!-- Theme CSS -->
    <link href="/css/agency.min.css" rel="stylesheet">
    <link href="/css/siczones.css" rel="stylesheet">
  </head>''') 
  print ('''
  <body>
      <!-- ==================== Nav Tabs ======================= -->
      <nav class="nav nav-tabs navbar-inverse navbar-fixed-top">
        <div class = "container">
        <ul class="nav nav-tabs">
          <li role="presentation"><a href="index.py">Home</a></li>
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
          <legend>Mode</legend>
          <h4 class="form-signin-heading">Configuration mode</h4>
          <hr class="colorgraph"><br>
      
      <!-- ========================== Data ========================= -->
      <div class="form-signin">
          <form action="#" class="btn-form">
          <button data-toggle="modal"  data-target="#login-modal-off" class="btn btn-lg btn-danger btn-block" Type="submit" VALUE="off" onmouseover="style.color='pink'" onmouseout="style.color='white'">
          OFF <span class="label label-success glyphicon glyphicon-ok pull-right"> </span>
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
          <form action="#" class="btn-form">
      <button data-toggle="modal"  data-target="#login-modal-basic" class="btn btn-lg btn-warning btn-block" Type="contact" VALUE="basic" onmouseover="style.color='yellow'" onmouseout="style.color='white'">
      BASIC<span class="label label-success glyphicon glyphicon-ok pull-right"> </span>
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
      <form action="#" class="btn-form">
        <button data-toggle="modal"  data-target="#login-modal-full" class="btn btn-lg btn-success btn-block" Type="contact" VALUE="full" onmouseover="style.color='#33FF33'" onmouseout="style.color='white'">
        FULL<span class="label label-success glyphicon glyphicon-ok pull-right"> </span>
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
      <form action="#" class="btn-form">
        <button data-toggle="modal"  data-target="#login-modal-advance" class="btn btn-lg btn-info btn-block" Type="contact" VALUE="advance" onmouseover="style.color='black'" onmouseout="style.color='white'">
        ADVANCE<span class="label label-success glyphicon glyphicon-ok pull-right"> </span>
          </button>
        <div class="modal fade" id="login-modal-advance" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true" style="display: none;">
        <div class="modal-dialog">
          <div class="loginmodal-container">
            <h4>Advance</h4><br>
            </br><button type="button" class="close" data-dismiss="modal">close[&times;]</button>         
          </div>
        </div>
        </div>    
      </form>
          </div>
      
          <br><form action="index.py"><button class="btn btn-lg btn-primary btn-block" VALUE="Back">Back</button></form>
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
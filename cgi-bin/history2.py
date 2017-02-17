#!/usr/bin/python 
# -*- coding: utf-8 -*-f
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

def readLog():
  infile = "../logfiles/alert.log" 
  with open(infile , "rU") as f:
      f = f.readlines()
  # print f
  for line in f:
      line = '<tr><td>'+line+'</td></tr>'
      print line

##Uncomment test readLog
#readLog()

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
<title>History</title>
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
<script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.4.8/angular.min.js"></script>

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
      <table class="table table-striped" >
        <thead>
            <tr>
              <th>
                      <div ng-app="myApp" ng-controller="namesCtrl">

                      <p>Type a letter in the input field:</p>

                      <p><input type="text" ng-model="test"></p>

                      <ul>
                        <li ng-repeat="x in names | filter:test">
                          {{ x }}
                        </li>
                      </ul>

                      </div>

                      <script>
                      angular.module('myApp', []).controller('namesCtrl', function($scope) {
                          $scope.names = [
                              'Jani',
                              'Carl',
                              'Margareth',
                          ];
                      });
                      </script>
              </th>
            </tr>
            <tr>
                <th><span> Date >>>>>>> Field : Value</span></th>
            </tr>
        </thead>
        <tbody>
  ''')   
  readLog() 
  print ('''
        </tbody>
      </table>
  </body>''')
  
  print ("</html>")
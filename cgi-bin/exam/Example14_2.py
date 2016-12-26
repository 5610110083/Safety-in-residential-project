#!/Python27/python 
import os 
print("Content-type: text/html\r\n\r\n") 
print("<font size=+1>Environment</font><br />") 
for param in os.environ.keys(): 
  print("<br><br>%20s</b>: %s<br />"%(param, os.environ[param])) 
#!/usr/bin/python

import time
import cgi, cgitb
import pigpio # abyz.co.uk/rpi/pigpio/python.html

print("Content-type: text/html") 
print("")  
print("<html><head>") 
print("") 
print("</head><body>") 
print("Hello from Python.") 
print("</body></html>") 
pin=4
pi = pigpio.pi() # Connect to local Pi.
pi.set_mode(pin, pigpio.OUTPUT)

for i in range(10):
   pi.write(pin, 1)
   #time.sleep(0.2)
   #pi.write(pin, 0)
   #time.sleep(0.2)
pi.stop() # Disconnect from local Pi.



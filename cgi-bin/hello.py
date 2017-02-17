#!/usr/bin/python 
# -*- coding: utf-8 -*-f
import os, time
# #===================== Start logCreate ======================#
def logCreate(login_status):
# When run as a cgi script, this will print the client's IP address.
	try:
		client_ip = cgi.escape(os.environ["REMOTE_ADDR"])
	except:
		client_ip = 'Unknow'
	with open("../logfiles/loginHistory.log", "a") as text_file:
		text_file.write("\r%s\t ip: %s %s" %(time.ctime(), client_ip, login_status))
	return
#logCreate('test')

user_agent = os.environ["HTTP_USER_AGENT"]
#===================== End logCreate ======================#
'''
infile = r"..\logfile\logCreate.log" 
with open(infile) as f:
    f = f.readlines()

def readLog():
  for line in f:
      line = '<p>'+line+'</p>'
      print line
'''


print("Content-type: text/html") 
print("")  
print("<html><head>") 
print("") 
print("</head><body>") 
print("Hello from Python.")
print user_agent 
#readLog()
print("</body></html>") 

'''

'''

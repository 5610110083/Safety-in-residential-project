#!/usr/bin/python 
from line import LineClient, LineGroup, LineContact
#import webbrowser
import urllib
import cgi, cgitb
form = cgi.FieldStorage()
try: 
	data = form.getvalue('data')
except:
	data = 'no data'
def sendText(i):
	USERNAME = 'sic@outlook.co.th'
	PASSWORD = '1234567896'
	GROUPNAME = 'Line-bot'
	#MSG = 'hello world!'

	#optional
	COMPUTERNEME = 'Siczones.Bot'
	TOKEN = ''
	try:
	  client = LineClient(id=USERNAME, password=PASSWORD, authToken=TOKEN, com_name=COMPUTERNEME)
	  TOKEN = client.authToken

	  client_group = client.getGroupByName(GROUPNAME)
	  #recent_group_msg = client_group.getRecentMessages(count=10)
	  #print "RecentMessages : %s\r\n" % recent_group_msg
	  client_group.sendMessage(":>> %s <<:\n Danger!!! \nsiczones-bot"%(i))
	  client_group.sendSticker(stickerId="3",stickerPackageId="1",stickerVersion="100")

	except:
	    print "Login Failed"

i = 0
while i < 1:
	a = sendText(data)
	i = i+1


print("Content-type: text/html") 
print("")  
print("<html><head>") 
print("<title>line notify</title>") 
print("</head><body>") 
print("%s Alert"%(data)) 
#print ('''<meta http-equiv="refresh" content="0.1;http://%s">'''%(homeIP))
print("</body></html>") 


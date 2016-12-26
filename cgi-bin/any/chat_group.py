#!/usr/bin/python
from line import LineClient, LineGroup, LineContact
#import webbrowser
import urllib

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
	  '''
	  if i < 1:
	  	print "TOKEN : %s\r\n" % TOKEN
	  '''

	  client_group = client.getGroupByName(GROUPNAME)
	  #recent_group_msg = client_group.getRecentMessages(count=10)
	  #print "RecentMessages : %s\r\n" % recent_group_msg
	  client_group.sendMessage(":>> %d <<:\n Oh No !!! \nsiczones-bot"%(i))
	  client_group.sendSticker(stickerId="3",stickerPackageId="1",stickerVersion="100")
	  #client.refreshGroups()
	  #client_group.sendMessage(MSG)
	  '''
	  op_list = []
	  for op in client.longPoll():
		op_list.append(op)
	  for op in op_list:
		sender   = op[0]
		receiver = op[1]
		message  = op[2]
	  msg = message.text
	  '''
	  #messages = client.groups[0].getRecentMessages(count=1)

	except:
	    print "Login Failed"

i = 0
while i < 1:
	a = sendText(i)
	i = i+1

'''
while True:
    op_list = []

    for op in client.longPoll():
        op_list.append(op)

    for op in op_list:
        sender   = op[0]
        receiver = op[1]
        message  = op[2]
        
        msg = message.text
        #msg = 'yes'
        by = "siczones bot"
        client_group.sendMessage("[%s] %s \n %s" % (sender.name, msg, by))

        if msg == "on":
          #webbrowser.open('http://192.168.0.103/?buttonallon')
          urllib.urlopen('http://192.168.0.101/?buttonallon')
          print "on success"
          client_group.sendMessage("on success")
        elif msg == "off":
          #webbrowser.open('http://192.168.0.103/?buttonalloff')
          urllib.urlopen('http://192.168.0.101/?buttonalloff')
          print "off success"
          client_group.sendMessage("off success")
'''
print("Content-type: text/html") 
print("")  
print("<html><head>") 
print("") 
print("</head><body>") 
print("Hello from Python.") 
print("</body></html>") 

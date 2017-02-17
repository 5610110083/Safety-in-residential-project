from datetime import datetime
import cgi
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
logCreate('test')
#===================== End logCreate ======================#

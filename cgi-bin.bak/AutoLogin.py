import time
import requests
import urllib

########################################################################
def connection():
    global status
    try:
        url = "https://www.google.com"
        urllib.urlopen(url)
        status = "Connected"
        return True
    except:
        status = "Disconnect"
        return False
########################################################################
def login():
    # Login
    url = 'https://securelogin.arubanetworks.com/auth/index.html/u'
    values = {'username': username,
              'password': password}
    try:
        r = requests.post(url, data=values)
        #print r.content
    except:
        print 'Connection failed.'
########################################################################

#scan input
print '============ Powered by Siczones ============'
print '** Please input PSU Passport !!'
print '   If not work,Please check PSU Passport.'
print '   And try again next time.'
print '============================================='

global username,password,sleep
#Sleep = <sleep> second (Active every <sleep>/60 minute)
sleep = float(raw_input("Refresh times(second): "))

while True:
    username = raw_input("Username: ")
    password = raw_input("Password: ")
    login()
    if connection() == True:
        print 'Login success.'
        break
    else:
        print 'Login failed. Please try again!'
print '============================================='
########################################################################
        
# Only run if the user types in "start"
# run = raw_input("Start? > ")
run = 'start'
mins = 0
hr = 0
if run == "start":
    while True:
        print status
        if connection() == False:
            login()
        print '>>>>>>>>>>>> running times : %d hr. %d minutes' %(hr, mins)
        time.sleep(sleep)
        mins += (sleep/60)
        if mins > 59:
            mins = 0
            hr += 1
########################################################################

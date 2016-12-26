#!/usr/bin/python
#Import modules for CGI handling  
import cgi, cgitb

# Create instance of FieldStorage  
form = cgi.FieldStorage()  
# Get data from fields 
Username = form.getvalue('Username') 
Password = form.getvalue('Password')
status = 0
print ("Content-type:text/html\r\n\r\n") 
print ("<html>")
if (Password == 'admin')&(Username == 'siczones'):
    status = 1
if status == 1:
    print ("<head>") 
    print ("<title>Welcome to server</title>") 
    print ("</head>") 
    print ("<body>")
    print ("<center><fieldset><legend>Hello !!</legend>")
    print ("<h2>Welcome to Siczones web login</h2>")
    #print ("<h2>Hello %s %s</h2>" % (Username, Password)) 
    print ("<h2>Hello %s</h2>" % (Username))
    print ('''<FORM><INPUT Type="button" VALUE="Log out" onClick="history.go(-1);return true;"></FORM>''')
    print ('''<FORM action="/UploadThingSpeak.html"><INPUT Type="submit" VALUE="Go to Upload data to ThingSpeak"></FORM>''')
    print ("</fieldset></center></body>") 
else:
    print ("<head>") 
    print ("<title>Try Agian</title>") 
    print ("</head>") 
    print ("<body><br/>")
    print ("<center>")
    print ("<fieldset><legend>Please try again!!</legend>")
    if "Username" not in form:
        print "<h2>No username was entered</h1>"
    if "Password" not in form:
        print "<h2>No password was entered</h1>"
    print ('''<FORM><INPUT Type="button" VALUE="Back" onClick="history.go(-1);return true;"></FORM>''')
    print ("</fieldset></center>")
    print ("</body>")
    
print ("</html>")

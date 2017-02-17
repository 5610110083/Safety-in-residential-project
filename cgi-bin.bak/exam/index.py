#!/Python27/python 
#Import modules for CGI handling  
import cgi, cgitb  
# Create instance of FieldStorage  
form = cgi.FieldStorage()  
# Get data from fields 
Username = form.getvalue('Username') 
Password  = form.getvalue('Password')
status = 0
if (Password == 'admin')&(Username == 'admin'):
    status = 1
if status == 1:
    print ("Content-type:text/html\r\n\r\n") 
    print ("<html>") 
    print ("<head>") 
    print ("<title>Hello - Second CGI Program</title>") 
    print ("</head>") 
    print ("<body>")
    print ("<center>")
    print ("<h2>Welcome to Siczones web login</h2>")
    print ("<center>")
    #print ("<h2>Hello %s %s</h2>" % (Username, Username)) 
    print ("</body>") 
    print ("</html>")
else:
    print ("Content-type:text/html\r\n\r\n") 
    print ("<html>") 
    print ("<head>") 
    print ("<title>Try Agian</title>") 
    print ("</head>") 
    print ("<body>")
    print ("<h2>Please Try Agian</h2>") 
    print ("</body>") 
    print ("</html>")

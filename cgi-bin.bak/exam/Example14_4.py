#!/Python27/python 
import cgi, cgitb  
form = cgi.FieldStorage()  
if form.getvalue('maths'): 
   math_flag = "ON" 
else: 
   math_flag = "OFF" 
if form.getvalue('physics'): 
   physics_flag = "ON" 
else: 
   physics_flag = "OFF" 
if form.getvalue('computer'): 
   computer_flag = "ON" 
else: 
   computer_flag = "OFF"  
print("Content-type:text/html\r\n\r\n") 
print("<html>") 
print("<head>") 
print("<title>Checkbox for CGI Program</title>") 
print("</head>") 
print("<body>") 
print("<h2> CheckBox Maths is : %s</h2>" % math_flag) 
print("<h2> CheckBox Physics is : %s</h2>" % physics_flag) 
print("<h2> CheckBox Computer is : %s</h2>" % computer_flag) 
print("</body>") 
print("</html>")